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

package org.openkilda.messaging.info.discovery;

import static com.google.common.base.MoreObjects.toStringHelper;

import org.openkilda.messaging.info.InfoData;
import org.openkilda.messaging.info.event.IslInfoData;
import org.openkilda.messaging.info.event.SwitchInfoData;
import org.openkilda.messaging.model.Flow;
import org.openkilda.messaging.model.ImmutablePair;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

import java.util.Objects;
import java.util.Set;

/**
 * Represents flow northbound response.
 */
@JsonSerialize
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
        "message_type",
        "requester",
        "switches",
        "isls",
        "flows"})
public class NetworkInfoData extends InfoData {
    /**
     * Serialization version number constant.
     */
    private static final long serialVersionUID = 1L;

    /**
     * Requester.
     */
    @JsonProperty("requester")
    protected String requester;

    /**
     * Switches.
     */
    @JsonProperty("switches")
    private Set<SwitchInfoData> switches;

    /**
     * ISLs.
     */
    @JsonProperty("isls")
    private Set<IslInfoData> isls;

    /**
     * Flows.
     */
    @JsonProperty("flows")
    private Set<ImmutablePair<Flow, Flow>> flows;

    /**
     * Default constructor.
     */
    public NetworkInfoData() {
    }

    /**
     * Instance constructor.
     *
     * @param requester requester
     * @param switches  switches
     * @param isls      isls
     * @param flows     flows
     */
    @JsonCreator
    public NetworkInfoData(@JsonProperty("requester") String requester,
                           @JsonProperty("switches") Set<SwitchInfoData> switches,
                           @JsonProperty("isls") Set<IslInfoData> isls,
                           @JsonProperty("flows") Set<ImmutablePair<Flow, Flow>> flows) {
        this.requester = requester;
        this.switches = switches;
        this.isls = isls;
        this.flows = flows;
    }

    /**
     * Returns requester.
     *
     * @return requester
     */
    public String getRequester() {
        return requester;
    }

    /**
     * Sets requester.
     *
     * @param requester requester
     */
    public void setRequester(String requester) {
        this.requester = requester;
    }

    /**
     * Returns switches.
     *
     * @return switches
     */
    public Set<SwitchInfoData> getSwitches() {
        return switches;
    }

    /**
     * Sets switches.
     *
     * @param switches switches
     */
    public void setSwitches(Set<SwitchInfoData> switches) {
        this.switches = switches;
    }

    /**
     * Returns isls.
     *
     * @return isls
     */
    public Set<IslInfoData> getIsls() {
        return isls;
    }

    /**
     * Sets isls.
     *
     * @param isls isls
     */
    public void setIsls(Set<IslInfoData> isls) {
        this.isls = isls;
    }

    /**
     * Returns flows.
     *
     * @return flows
     */
    public Set<ImmutablePair<Flow, Flow>> getFlows() {
        return flows;
    }

    /**
     * Sets flows.
     *
     * @param flows flows
     */
    public void setFlows(Set<ImmutablePair<Flow, Flow>> flows) {
        this.flows = flows;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String toString() {
        return toStringHelper(this)
                .add("requester", requester)
                .add("switches", switches)
                .add("isls", isls)
                .add("flows", flows)
                .toString();
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public int hashCode() {
        return Objects.hash(requester, switches, isls, flows);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public boolean equals(Object object) {
        if (this == object) {
            return true;
        }
        if (object == null || getClass() != object.getClass()) {
            return false;
        }

        NetworkInfoData that = (NetworkInfoData) object;
        return Objects.equals(getRequester(), that.getRequester())
                && Objects.equals(getSwitches(), that.getSwitches())
                && Objects.equals(getIsls(), that.getIsls())
                && Objects.equals(getFlows(), that.getFlows());
    }
}
