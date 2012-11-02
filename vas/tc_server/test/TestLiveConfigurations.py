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


from vas.tc_server.Instances import Instance
from vas.tc_server.LiveConfigurations import LiveConfigurations, LiveConfiguration
from vas.tc_server.NodeLiveConfigurations import NodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(LiveConfigurations(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/live/'), 3)

    def test_detail(self):
        self._assert_item(LiveConfiguration(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/live/2/'), [
            ('path', 'conf/server.xml'),
            ('size', 10537),
            ('content', 'groups-instances-configurations-live-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, Instance)),
            ('node_configurations', [
                NodeLiveConfiguration(self._client,
                    'https://localhost:8443/tc-server/v1/nodes/0/instances/4/configurations/live/7/'),
                NodeLiveConfiguration(self._client,
                    'https://localhost:8443/tc-server/v1/nodes/0/instances/3/configurations/live/6/')])
        ])
