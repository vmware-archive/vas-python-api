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


from vas.gemfire.Groups import Group
from vas.gemfire.Installations import Installation
from vas.gemfire.AgentInstances import AgentInstances, AgentInstance
from vas.gemfire.AgentLiveConfigurations import AgentLiveConfigurations
from vas.gemfire.AgentNodeInstances import AgentNodeInstance
from vas.gemfire.AgentPendingConfigurations import AgentPendingConfigurations
from vas.test.VasTestCase import VasTestCase

class TestAgentInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            AgentInstances(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/'))

    def test_create(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/gemfire/v1/groups/0/agent-instances/'
        self._return_location('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/')

        instance = AgentInstances(self._client, location).create(Installation(self._client, installation_location),
            'example')

        self.assertIsInstance(instance, AgentInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location}, 'agent-group-instance')

    def test_detail(self):
        self._assert_item(
            AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/'), [
                ('name', 'example'),
                ('state', 'STOPPED'),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, AgentLiveConfigurations)),
                ('node_instances', [
                    AgentNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/5/'),
                    AgentNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/1/agent-instances/6/')
                ]),
                ('pending_configurations', lambda actual: self.assertIsInstance(actual, AgentPendingConfigurations))
            ])

    def test_start_parallel(self):
        AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/').start()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/').start(True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/').stop()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/').stop(True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/'

        AgentInstance(self._client, location).update(Installation(self._client, installation_location))

        self._assert_post(location, {'installation': installation_location})

    def test_delete(self):
        self._assert_deletable(
            AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/'))
