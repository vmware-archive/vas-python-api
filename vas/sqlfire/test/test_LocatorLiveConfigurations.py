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


from vas.sqlfire.LocatorInstances import LocatorInstance
from vas.sqlfire.LocatorLiveConfigurations import LocatorLiveConfigurations, LocatorLiveConfiguration
from vas.sqlfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestLocatorLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(LocatorLiveConfigurations(self._client,
            'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/1/configurations/live/'), 1)

    def test_detail(self):
        self._assert_item(LocatorLiveConfiguration(self._client,
            'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/1/configurations/live/2/'), [
            ('path', 'sqlfire.properties'),
            ('size', 10537),
            ('content', 'groups-locator-instances-configurations-live-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, LocatorInstance)),
            ('node_configurations', [
                LocatorNodeLiveConfiguration(self._client,
                    'https://localhost:8443/sqlfire/v1/nodes/0/locator-instances/4/configurations/live/7/'),
                LocatorNodeLiveConfiguration(self._client,
                    'https://localhost:8443/sqlfire/v1/nodes/0/locator-instances/3/configurations/live/6/')])
        ])
