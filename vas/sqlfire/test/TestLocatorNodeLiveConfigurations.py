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


from vas.sqlfire.LocatorLiveConfigurations import LocatorLiveConfiguration
from vas.sqlfire.LocatorNodeInstances import LocatorNodeInstance
from vas.sqlfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfigurations, LocatorNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestLocatorNodeLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(LocatorNodeLiveConfigurations(self._client,
            'https://localhost:8443/sqlfire/v1/nodes/2/locator-instances/3/configurations/live/'), 1)

    def test_detail(self):
        self._assert_item(LocatorNodeLiveConfiguration(self._client,
            'https://localhost:8443/sqlfire/v1/nodes/0/locator-instances/3/configurations/live/5/'), [
            ('path', 'sqlfire.properties'),
            ('size', 3412),
            ('group_configuration', lambda actual: self.assertIsInstance(actual, LocatorLiveConfiguration)),
            ('instance', lambda actual: self.assertIsInstance(actual, LocatorNodeInstance)),
            ('content', 'nodes-locator-instances-configurations-live-content\n')
        ])
