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


from vas.gemfire.CacheServerInstances import CacheServerInstance
from vas.gemfire.CacheServerLiveConfigurations import CacheServerLiveConfigurations, CacheServerLiveConfiguration
from vas.gemfire.CacheServerNodeLiveConfigurations import CacheServerNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestCacheServerLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(CacheServerLiveConfigurations(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/live/'))

    def test_detail(self):
        self._assert_item(CacheServerLiveConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/live/2/'), [
            ('path', 'gemfire.properties'),
            ('size', 10537),
            ('content', 'groups-cache-server-instances-configurations-live-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, CacheServerInstance)),
            ('node_configurations', [
                CacheServerNodeLiveConfiguration(self._client,
                    'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/4/configurations/live/7/'),
                CacheServerNodeLiveConfiguration(self._client,
                    'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/configurations/live/6/')])
        ])
