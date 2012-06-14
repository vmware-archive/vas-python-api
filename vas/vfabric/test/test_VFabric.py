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


from vas.shared.Nodes import Nodes
from vas.test.test_TestRoot import TestRoot
from vas.vfabric.AgentImage import AgentImage
from vas.vfabric.VFabric import VFabric

class TestVFabric(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['https://localhost:8443/vfabric/v1'] = {
        'links': [{
            'rel': 'agent-image',
            'href': 'agent-image-href'
        }, {
            'rel': 'nodes',
            'href': 'nodes-href'
        }, {
            'rel': 'tasks',
            'href': 'tasks-href'
        }]
    }

    _PAYLOADS['agent-image-href'] = {
        'links': [{
            'rel': 'content',
            'href': 'content-href'
        }, {
            'rel': 'security',
            'href': 'security-href'
        }, {
            'rel': 'self',
            'href': 'self-href'
        }]
    }

    _PAYLOADS['nodes-href'] = {
        'nodes': [],
        'links': [{
            'rel': 'security',
            'href': 'security-href'
        }, {
            'rel': 'self',
            'href': 'self-href'
        }]
    }

    def setUp(self):
        super(TestVFabric, self).setUp()
        self.__vfabric = VFabric(self._client, 'https://localhost:8443{}')

    def test_agent_image(self):
        self.assertIsInstance(self.__vfabric.agent_image, AgentImage)

    def test_nodes(self):
        self.assertIsInstance(self.__vfabric.nodes, Nodes)
