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


from vas.sqlfire.ServerInstances import ServerInstance
from vas.sqlfire.ServerLogs import ServerLogs
from vas.sqlfire.ServerNodeInstances import ServerNodeInstances, ServerNodeInstance
from vas.sqlfire.ServerNodeLiveConfigurations import ServerNodeLiveConfigurations
from vas.sqlfire.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestServerNodeInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            ServerNodeInstances(self._client, 'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/'))

    def test_detail(self):
        self._assert_item(
            ServerNodeInstance(self._client,
                'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/'), [
                ('bind_address', 'bind.address'),
                ('client_bind_address', 'client.bind.address'),
                ('client_port', 1234),
                ('critical_heap_percentage', 90),
                ('group_instance', lambda actual: self.assertIsInstance(actual, ServerInstance)),
                ('initial_heap', "1024M"),
                ('jvm_options', ['-Da=alpha']),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, ServerNodeLiveConfigurations)),
                ('logs', lambda actual: self.assertIsInstance(actual, ServerLogs)),
                ('max_heap', '1024M'),
                ('name', 'example'),
                ('node', lambda actual: self.assertIsInstance(actual, Node)),
                ('run_netserver', lambda actual: self.assertTrue(actual)),
                ('state', 'STOPPED'),
            ])

    def test_start_rebalanced(self):
        ServerNodeInstance(self._client,
            'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/').start(True)
        self._assert_post('https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/state/',
            {'status': 'STARTED', 'rebalance': True})

    def test_start_not_rebalanced(self):
        ServerNodeInstance(self._client,
            'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/').start(False)
        self._assert_post('https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/state/',
            {'status': 'STARTED', 'rebalance': False})

    def test_stop(self):
        ServerNodeInstance(self._client,
            'https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/').stop()
        self._assert_post('https://localhost:8443/sqlfire/v1/nodes/0/server-instances/3/state/',
            {'status': 'STOPPED'})
