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


from vas.shared.Node import Node
from vas.test.test_TestRoot import TestRoot

class TestNode(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['node-href'] = {
        'agent-home': 'agent-home',
        'architecture': 'architecture',
        'host-names': ['host-name-1', 'host-name-2'],
        'ip-addresses': ['ip-address-1', 'ip-address-2'],
        'metadata': {'key', 'value'},
        'operating-system': 'operating-system',
        'links': [{
            'rel': 'self',
            'href': 'self-href'
        }, {
            'rel': 'security',
            'href': 'security-href'
        }]
    }

    def setUp(self):
        super(TestNode, self).setUp()
        self.__node = Node(self._client, 'node-href')

    def test_attributes(self):
        self.assertEqual('agent-home', self.__node.agent_home)
        self.assertEqual('architecture', self.__node.architecture)
        self.assertEqual(['host-name-1', 'host-name-2'], self.__node.host_names)
        self.assertEqual(['ip-address-1', 'ip-address-2'], self.__node.ip_addresses)
        self.assertEqual({'key', 'value'}, self.__node.metadata)
        self.assertEqual('operating-system', self.__node.operating_system)