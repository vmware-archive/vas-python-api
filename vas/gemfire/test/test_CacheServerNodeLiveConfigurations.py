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


from vas.gemfire.CacheServerLiveConfigurations import CacheServerLiveConfiguration
from vas.gemfire.CacheServerNodeInstances import CacheServerNodeInstance
from vas.gemfire.CacheServerNodeLiveConfigurations import CacheServerNodeLiveConfigurations, CacheServerNodeLiveConfiguration
from vas.test.VasTestCase import VasTestCase

class TestCacheServerNodeLiveConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(CacheServerNodeLiveConfigurations(self._client,
            'https://localhost:8443/gemfire/v1/nodes/2/cache-server-instances/3/configurations/live/'))

    def test_detail(self):
        self._assert_item(CacheServerNodeLiveConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/configurations/live/5/'), [
            ('path', 'gemfire.properties'),
            ('size', 3412),
            ('group_configuration', lambda actual: self.assertIsInstance(actual, CacheServerLiveConfiguration)),
            ('instance', lambda actual: self.assertIsInstance(actual, CacheServerNodeInstance)),
            ('content', 'nodes-cache-server-instances-configurations-live-content\n')
        ])
