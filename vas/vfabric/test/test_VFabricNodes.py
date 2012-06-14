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


from vas.test.test_TestRoot import TestRoot
from vas.vfabric.VFabricNode import VFabricNode
from vas.vfabric.VFabricNodes import VFabricNodes

class TestVFabricNodes(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['nodes-href'] = {
        'nodes': [{
            'links': [{
                'rel': 'self',
                'href': 'self-href'
            }, {
                'rel': 'security',
                'href': 'security-href'
            }]
        }],
        'links': [{
            'rel': 'self',
            'href': 'self-href'
        }, {
            'rel': 'security',
            'href': 'security-href'
        }]
    }

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
        super(TestVFabricNodes, self).setUp()
        self.__nodes = VFabricNodes(self._client, 'nodes-href')

    def test__create_item(self):
        self.assertIsInstance(self.__nodes._create_item('node-href'), VFabricNode)