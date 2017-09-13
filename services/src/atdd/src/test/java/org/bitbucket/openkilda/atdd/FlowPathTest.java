package org.bitbucket.openkilda.atdd;

import static org.bitbucket.openkilda.flow.FlowUtils.dumpLinks;
import static org.bitbucket.openkilda.flow.FlowUtils.getLinkBandwidth;
import static org.junit.Assert.assertEquals;

import org.bitbucket.openkilda.flow.FlowUtils;
import org.bitbucket.openkilda.messaging.info.event.IslInfoData;
import org.bitbucket.openkilda.messaging.info.event.PathInfoData;
import org.bitbucket.openkilda.messaging.info.event.PathNode;
import org.bitbucket.openkilda.messaging.model.Flow;
import org.bitbucket.openkilda.messaging.model.ImmutablePair;
import org.bitbucket.openkilda.topo.TopologyHelp;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

import java.io.File;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.List;


public class FlowPathTest {
    private static final String fileName = "topologies/multi-path-topology.json";
    private static final List<ImmutablePair<String, String>> shortestPathLinks = Arrays.asList(
            new ImmutablePair<>("00:00:00:00:00:00:00:07", "1"), new ImmutablePair<>("00:00:00:00:00:00:00:03", "2"),
            new ImmutablePair<>("00:00:00:00:00:00:00:02", "2"), new ImmutablePair<>("00:00:00:00:00:00:00:03", "1"));
    private static final List<ImmutablePair<String, String>> alternativePathLinks = Arrays.asList(
            new ImmutablePair<>("00:00:00:00:00:00:00:02", "3"), new ImmutablePair<>("00:00:00:00:00:00:00:04", "1"),
            new ImmutablePair<>("00:00:00:00:00:00:00:05", "1"), new ImmutablePair<>("00:00:00:00:00:00:00:04", "2"),
            new ImmutablePair<>("00:00:00:00:00:00:00:05", "2"), new ImmutablePair<>("00:00:00:00:00:00:00:06", "1"),
            new ImmutablePair<>("00:00:00:00:00:00:00:06", "2"), new ImmutablePair<>("00:00:00:00:00:00:00:07", "3"));
    private static final ImmutablePair<PathInfoData, PathInfoData> expectedPath = new ImmutablePair<>(
            new PathInfoData(0L, Arrays.asList(
                    new PathNode("00:00:00:00:00:00:00:02", 2, 0, 0L),
                    new PathNode("00:00:00:00:00:00:00:03", 1, 1, 0L),
                    new PathNode("00:00:00:00:00:00:00:03", 2, 2, 0L),
                    new PathNode("00:00:00:00:00:00:00:07", 1, 3, 0L))),
            new PathInfoData(0L, Arrays.asList(
                    new PathNode("00:00:00:00:00:00:00:07", 1, 0, 0L),
                    new PathNode("00:00:00:00:00:00:00:03", 2, 1, 0L),
                    new PathNode("00:00:00:00:00:00:00:03", 1, 2, 0L),
                    new PathNode("00:00:00:00:00:00:00:02", 2, 3, 0L))));

    private long pre_start;
    private long start;

    @Given("^a multi-path topology$")
    public void a_multi_path_topology() throws Throwable {
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource(fileName).getFile());
        String json = new String(Files.readAllBytes(file.toPath()));

        pre_start = System.currentTimeMillis();
        assert TopologyHelp.CreateMininetTopology(json);
        start = System.currentTimeMillis();
    }

    @When("^all links have available bandwidth (\\d+)$")
    public void checkAvailableBandwidth(int expectedAvailableBandwidth) throws Exception {
        List<IslInfoData> links = dumpLinks();
        for (IslInfoData link : links) {
            assertEquals(expectedAvailableBandwidth, link.getAvailableBandwidth());
        }
    }

    @Then("^shortest path links available bandwidth have available bandwidth (\\d+)$")
    public void checkShortestPathAvailableBandwidthDecreased(int expectedAvailableBandwidth) throws Exception {
        for (ImmutablePair<String, String> expectedLink : shortestPathLinks) {
            Integer actualBandwidth = getLinkBandwidth(expectedLink.getLeft(), expectedLink.getRight());
            assertEquals(expectedAvailableBandwidth, actualBandwidth.intValue());
        }
    }

    @Then("^alternative path links available bandwidth have available bandwidth (\\d+)$")
    public void checkAlternativePathAvailableBandwidthDecreased(int expectedAvailableBandwidth) throws Exception {
        for (ImmutablePair<String, String> expectedLink : alternativePathLinks) {
            Integer actualBandwidth = getLinkBandwidth(expectedLink.getLeft(), expectedLink.getRight());
            assertEquals(expectedAvailableBandwidth, actualBandwidth.intValue());
        }
    }

    @Then("^flow (.*) with (.*) (\\d+) (\\d+) and (.*) (\\d+) (\\d+) and (\\d+) path correct$")
    public void flowPathCorrect(String flowId, String sourceSwitch, int sourcePort, int sourceVlan,
                                String destinationSwitch, int destinationPort, int destinationVlan, int bandwidth)
            throws Exception {
        Flow flow = new Flow(FlowUtils.getFlowName(flowId), bandwidth, flowId, sourceSwitch,
                sourcePort, sourceVlan, destinationSwitch, destinationPort, destinationVlan);
        ImmutablePair<PathInfoData, PathInfoData> path = FlowUtils.getFlowPath(flow);
        System.out.println(path);
        assertEquals(expectedPath, path);
    }
}
