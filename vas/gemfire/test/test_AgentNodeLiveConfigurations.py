# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.gemfire.AgentLiveConfigurations import AgentLiveConfiguration
from vas.gemfire.AgentNodeInstances import AgentNodeInstance
from vas.gemfire.AgentNodeLiveConfigurations import AgentNodeLiveConfigurations, AgentNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestAgentNodeLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(AgentNodeLiveConfigurations(self._client,
            'https://localhost:8443/gemfire/v1/nodes/2/agent-instances/3/configurations/live/'), 1)

    def test_detail(self):
        self._assert_item(AgentNodeLiveConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/configurations/live/5/'), [
            ('path', 'agent.properties'),
            ('size', 3412),
            ('group_configuration', lambda actual: self.assertIsInstance(actual, AgentLiveConfiguration)),
            ('instance', lambda actual: self.assertIsInstance(actual, AgentNodeInstance)),
            ('content', 'nodes-agent-instances-configurations-live-content\n')
        ])
