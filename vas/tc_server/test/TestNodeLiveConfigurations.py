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


from vas.tc_server.LiveConfigurations import LiveConfiguration
from vas.tc_server.NodeInstances import NodeInstance
from vas.tc_server.NodeLiveConfigurations import NodeLiveConfigurations, NodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestNodeLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(NodeLiveConfigurations(self._client,
            'https://localhost:8443/tc-server/v1/nodes/2/instances/3/configurations/live/'), 3)

    def test_detail(self):
        self._assert_item(NodeLiveConfiguration(self._client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/configurations/live/5/'), [
            ('path', 'conf/server.xml'),
            ('size', 3412),
            ('group_configuration', lambda actual: self.assertIsInstance(actual, LiveConfiguration)),
            ('instance', lambda actual: self.assertIsInstance(actual, NodeInstance)),
            ('content', 'nodes-instances-configurations-live-content\n')
        ])
