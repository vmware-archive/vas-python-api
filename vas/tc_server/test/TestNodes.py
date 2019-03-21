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


from vas.tc_server.Groups import Group
from vas.tc_server.NodeInstances import NodeInstances
from vas.tc_server.Nodes import Nodes, Node
from vas.test.VasTestCase import VasTestCase

class TestNodes(VasTestCase):
    def test_list(self):
        self._assert_collection(Nodes(self._client, 'https://localhost:8443/tc-server/v1/nodes/'))

    def test_detail(self):
        self._assert_item(Node(self._client, 'https://localhost:8443/tc-server/v1/nodes/0/'), [
            ('agent_home', '/opt/vmware/vfabric-administration-agent'),
            ('architecture', 'x64'),
            ('groups', [Group(self._client, 'https://localhost:8443/tc-server/v1/groups/2/'),
                        Group(self._client, 'https://localhost:8443/tc-server/v1/groups/1/')]),
            ('host_names', ['example-host']),
            ('instances', lambda actual: self.assertIsInstance(actual, NodeInstances)),
            ('ip_addresses', ['fc00:192:168:0:2d:4fff:fd48:5e80', '192.168.0.2']),
            ('ipv4_addresses', ['192.168.0.2']),
            ('ipv6_addresses', ['fc00:192:168:0:2d:4fff:fd48:5e80']),
            ('java_home', '/usr/bin'),
            ('metadata', {'a': 'alpha', 'b': 'bravo'}),
            ('operating_system', 'Linux')
        ])

    def test_update(self):
        location = 'https://localhost:8443/tc-server/v1/nodes/0/'

        Node(self._client, location).update({'foo': 'bar'})
        self._assert_post(location, {'metadata': {'foo': 'bar'}})
