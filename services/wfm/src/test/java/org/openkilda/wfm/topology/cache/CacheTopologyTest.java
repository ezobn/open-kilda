/* Copyright 2017 Telstra Open Source
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

package org.openkilda.wfm.topology.cache;

import static org.openkilda.messaging.Utils.DEFAULT_CORRELATION_ID;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import org.openkilda.messaging.Destination;
import org.openkilda.messaging.Topic;
import org.openkilda.messaging.command.CommandMessage;
import org.openkilda.messaging.command.flow.FlowRestoreRequest;
import org.openkilda.messaging.info.InfoMessage;
import org.openkilda.messaging.info.discovery.NetworkInfoData;
import org.openkilda.messaging.info.event.SwitchInfoData;
import org.openkilda.messaging.info.event.SwitchState;
import org.openkilda.messaging.info.flow.FlowInfoData;
import org.openkilda.messaging.info.flow.FlowOperation;
import org.openkilda.messaging.model.Flow;
import org.openkilda.messaging.model.ImmutablePair;
import org.openkilda.wfm.AbstractStormTest;
import org.openkilda.wfm.topology.TestKafkaConsumer;
import org.openkilda.wfm.topology.Topology;
import org.openkilda.wfm.topology.event.OFEventWFMTopology;

import com.fasterxml.jackson.databind.ObjectMapper;
import edu.emory.mathcs.backport.java.util.Collections;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.storm.Config;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.utils.Utils;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

public class CacheTopologyTest extends AbstractStormTest {
    private static final ObjectMapper objectMapper = new ObjectMapper();
    private static final String firstFlowId = "first-flow";
    private static final String secondFlowId = "second-flow";
    private static final String thirdFlowId = "third-flow";
    private static final SwitchInfoData sw = new SwitchInfoData("sw",
            SwitchState.ADDED, "127.0.0.1", "localhost", "test switch", "kilda");
    private static final ImmutablePair<Flow, Flow> firstFlow = new ImmutablePair<>(
            new Flow(firstFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2),
            new Flow(firstFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2));
    private static final ImmutablePair<Flow, Flow> secondFlow = new ImmutablePair<>(
            new Flow(secondFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2),
            new Flow(secondFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2));
    private static final ImmutablePair<Flow, Flow> thirdFlow = new ImmutablePair<>(
            new Flow(thirdFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2),
            new Flow(thirdFlowId, 10000, "", "test-switch", 1, 2, "test-switch", 1, 2));
    private static final Set<ImmutablePair<Flow, Flow>> flows = new HashSet<>();
    private static final NetworkInfoData dump = new NetworkInfoData(
            "test", Collections.emptySet(), Collections.emptySet(), flows);

    private static TestKafkaConsumer teConsumer;
    private static TestKafkaConsumer flowConsumer;

    @BeforeClass
    public static void setupOnce() throws Exception {
        AbstractStormTest.setupOnce();
        File file = new File(CacheTopologyTest.class.getResource(Topology.TOPOLOGY_PROPERTIES).getFile());
        CacheTopology cacheTopology = new CacheTopology(file);
        StormTopology stormTopology = cacheTopology.createTopology();
        Config config = stormConfig();
        cluster.submitTopology(CacheTopologyTest.class.getSimpleName(), config, stormTopology);

        teConsumer = new TestKafkaConsumer(Topic.TEST.getId(), Destination.TOPOLOGY_ENGINE,
                kafkaProperties(UUID.nameUUIDFromBytes(Destination.TOPOLOGY_ENGINE.toString().getBytes()).toString()));
        teConsumer.start();

        flowConsumer = new TestKafkaConsumer(CacheTopology.STATE_DUMP_TOPIC, Destination.WFM,
                kafkaProperties(UUID.nameUUIDFromBytes(Destination.WFM.toString().getBytes()).toString()));
        flowConsumer.start();

        Utils.sleep(10000);

        System.out.println("Waiting For Dump Request");
        TimeUnit.SECONDS.sleep(OFEventWFMTopology.DEFAULT_DISCOVERY_TIMEOUT);

        System.out.println("Waited For Dump Request");
        teConsumer.pollMessage();
    }

    @AfterClass
    public static void teardownOnce() throws Exception {
        cluster.killTopology(CacheTopologyTest.class.getSimpleName());
        Utils.sleep(4 * 1000);
        AbstractStormTest.teardownOnce();
    }

    @Test
    public void cacheReceivesFlowTopologyUpdatesAndSendsToTopologyEngine() throws Exception {
        System.out.println("Flow Update Test");

        sendFlowUpdate(thirdFlow);

        ConsumerRecord<String, String> flow = teConsumer.pollMessage();

        assertNotNull(flow);
        assertNotNull(flow.value());

        InfoMessage infoMessage = objectMapper.readValue(flow.value(), InfoMessage.class);
        FlowInfoData infoData = (FlowInfoData) infoMessage.getData();
        assertNotNull(infoData);

        assertEquals(thirdFlow, infoData.getPayload());
    }

    @Test
    public void cacheReceivesWfmTopologyUpdatesAndSendsToTopologyEngine() throws Exception {
        System.out.println("Network Update Test");

        sendSwitchUpdate(sw);

        ConsumerRecord<String, String> record = teConsumer.pollMessage();

        assertNotNull(record);
        assertNotNull(record.value());

        InfoMessage infoMessage = objectMapper.readValue(record.value(), InfoMessage.class);
        SwitchInfoData data = (SwitchInfoData) infoMessage.getData();
        assertNotNull(data);

        assertEquals(sw, data);
    }

    @Test
    public void cacheReceivesNetworkDumpAndSendsToFlowTopology() throws Exception {
        System.out.println("Dump Test");

        Set<String> flowIds = new HashSet<>(Arrays.asList(firstFlowId, secondFlowId));
        flows.add(firstFlow);
        flows.add(secondFlow);

        sendNetworkDump(dump);

        ConsumerRecord<String, String> firstRecord = flowConsumer.pollMessage();
        ConsumerRecord<String, String> secondRecord = flowConsumer.pollMessage();

        assertNotNull(firstRecord);
        assertNotNull(firstRecord.value());

        CommandMessage commandMessage = objectMapper.readValue(firstRecord.value(), CommandMessage.class);
        FlowRestoreRequest commandData = (FlowRestoreRequest) commandMessage.getData();
        assertNotNull(commandData);
        assertTrue(flowIds.contains(commandData.getPayload().getLeft().getFlowId()));

        assertNotNull(secondRecord);
        assertNotNull(secondRecord.value());

        commandMessage = objectMapper.readValue(secondRecord.value(), CommandMessage.class);
        commandData = (FlowRestoreRequest) commandMessage.getData();
        assertNotNull(commandData);
        assertTrue(flowIds.contains(commandData.getPayload().getLeft().getFlowId()));
    }

    private void sendMessage(Object object, String topic) throws IOException {
        String request = objectMapper.writeValueAsString(object);
        kProducer.pushMessage(topic, request);
    }

    private void sendNetworkDump(NetworkInfoData data) throws IOException {
        System.out.println("Topology-Engine: Send Network Dump");
        InfoMessage info = new InfoMessage(data, 0, DEFAULT_CORRELATION_ID, Destination.WFM_CACHE);
        sendMessage(info, Topic.TEST.getId());
    }

    private void sendSwitchUpdate(SwitchInfoData sw) throws IOException {
        System.out.println("Wfm Topology: Send Switch Add Request");
        sendMessage(sw, CacheTopology.STATE_UPDATE_TOPIC);
    }

    private void sendFlowUpdate(ImmutablePair<Flow, Flow> flow) throws IOException {
        System.out.println("Flow Topology: Send Flow Creation Request");
        FlowInfoData data = new FlowInfoData(flow.getLeft().getFlowId(),
                flow, FlowOperation.CREATE, DEFAULT_CORRELATION_ID);
        sendMessage(data, CacheTopology.STATE_UPDATE_TOPIC);
    }
}
