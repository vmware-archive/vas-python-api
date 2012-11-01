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
from vas.gemfire.CacheServerPendingConfigurations import CacheServerPendingConfigurations, CacheServerPendingConfiguration
from vas.test.VasTestCase import VasTestCase

class TestCacheServerPendingConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(CacheServerPendingConfigurations(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/'))

    def test_create(self):
        location = 'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/'
        self._return_location(
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/2/')

        pending_configuration = CacheServerPendingConfigurations(self._client, location).create('conf/server.xml',
            'configuration-content')

        self.assertIsInstance(pending_configuration, CacheServerPendingConfiguration)
        self._assert_post_multipart(location, 'configuration-content', {'path': 'conf/server.xml'})

    def test_detail(self):
        self._assert_item(CacheServerPendingConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/2/'), [
            ('path', 'gemfire.properties'),
            ('size', 10537),
            ('content', 'groups-cache-server-instances-configurations-pending-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, CacheServerInstance))
        ])

    def test_set_content(self):
        #noinspection PyPropertyAccess
        CacheServerPendingConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/2/').content = 'new-content'
        self._assert_post(
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/2/content/',
            'new-content')


    def test_delete(self):
        self._assert_deletable(CacheServerPendingConfiguration(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/configurations/pending/2/'))