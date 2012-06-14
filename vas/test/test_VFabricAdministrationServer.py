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


from vas.VFabricAdministrationServer import VFabricAdministrationServer
from vas.tc_server.TcServer import TcServer
from vas.test.test_TestRoot import TestRoot
from vas.vfabric.VFabric import VFabric

class TestVFabricAdministrationServer(TestRoot):
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

    def setUp(self):
        super(TestVFabricAdministrationServer, self).setUp()
        self.__vfabric_administration_server = VFabricAdministrationServer(client=self._client)

    def test_vfabric(self):
        self.assertIsInstance(self.__vfabric_administration_server.vfabric, VFabric)
