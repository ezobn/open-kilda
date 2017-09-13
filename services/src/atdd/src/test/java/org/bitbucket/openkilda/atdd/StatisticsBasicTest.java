package org.bitbucket.openkilda.atdd;

import static org.bitbucket.openkilda.DefaultParameters.opentsdbEndpoint;
import static org.bitbucket.openkilda.flow.FlowUtils.getTimeDuration;
import static org.junit.Assert.assertNotEquals;

import org.bitbucket.openkilda.messaging.model.Metric;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import cucumber.api.java.en.Then;
import org.glassfish.jersey.client.ClientConfig;

import java.util.List;
import java.util.concurrent.TimeUnit;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.core.Response;

public class StatisticsBasicTest {

    public boolean test = false;

    public StatisticsBasicTest() {
    }

    private List<Metric> getNumberOfDatapoints() throws Throwable {
        long current = System.currentTimeMillis();
        Client client = ClientBuilder.newClient(new ClientConfig());
        Response response = client
                .target(opentsdbEndpoint)
                .path("/api/query")
                .queryParam("start", "4h-ago")
                .queryParam("m", "sum:pen.switch.tx-bytes")
                .queryParam("timezone", "Australia/Melbourne")
                .request().get();

        System.out.println("\n== OpenTSDB Metrics request");
        System.out.println(String.format("==> response = %s", response));
        System.out.println(String.format("==> OpenTSDB Metrics Time: %,.3f", getTimeDuration(current)));

        List<Metric> metrics = new ObjectMapper().readValue(
                response.readEntity(String.class), new TypeReference<List<Metric>>() {
                });

        System.out.println(String.format("===> Metrics = %s", metrics));

        return metrics;
    }

    @Then("^data go to database$")
    public void dataCreated() throws Throwable {
        TimeUnit.SECONDS.sleep(10);
        List<Metric> result = getNumberOfDatapoints();
        assertNotEquals(result, 0);
    }

    @Then("^database keeps growing$")
    public void database_keeps_growing() throws Throwable {
        List<Metric> result1 = getNumberOfDatapoints();
        // floodlight-modules statistics gathering interval
        TimeUnit.SECONDS.sleep(10);
        List<Metric> result2 = getNumberOfDatapoints();
        assertNotEquals(result1, result2);
    }
}
