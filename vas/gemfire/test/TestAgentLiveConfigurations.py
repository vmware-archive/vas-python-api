# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.gemfire.AgentInstances import AgentInstance
from vas.gemfire.AgentLiveConfigurations import AgentLiveConfigurations, AgentLiveConfiguration
from vas.gemfire.AgentNodeLiveConfigurations import AgentNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestAgentLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(AgentLiveConfigurations(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/agent-instances/1/configurations/live/'), 1)

    def test_detail(self):
        self._assert_item(AgentLiveConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/agent-instances/1/configurations/live/2/'), [
            ('path', 'agent.properties'),
            ('size', 10537),
            ('content', 'groups-agent-instances-configurations-live-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, AgentInstance)),
            ('node_configurations', [
                AgentNodeLiveConfiguration(self._client,
                    'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/configurations/live/6/'),
                AgentNodeLiveConfiguration(self._client,
                    'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/4/configurations/live/7/')])
        ])
