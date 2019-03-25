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
from vas.gemfire.AgentLogs import AgentLogs
from vas.gemfire.AgentNodeInstances import AgentNodeInstances, AgentNodeInstance
from vas.gemfire.AgentNodeLiveConfigurations import AgentNodeLiveConfigurations
from vas.gemfire.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestAgentNodeInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            AgentNodeInstances(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/'))

    def test_detail(self):
        self._assert_item(
            AgentNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/'), [
                ('group_instance', lambda actual: self.assertIsInstance(actual, AgentInstance)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, AgentNodeLiveConfigurations)),
                ('logs', lambda actual: self.assertIsInstance(actual, AgentLogs)),
                ('name', 'example'),
                ('node', lambda actual: self.assertIsInstance(actual, Node)),
                ('state', 'STOPPED')
            ])

    def test_start(self):
        AgentNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/').start()
        self._assert_post('https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/state/', {'status': 'STARTED'})

    def test_stop(self):
        AgentNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/').stop()
        self._assert_post('https://localhost:8443/gemfire/v1/nodes/0/agent-instances/3/state/', {'status': 'STOPPED'})
