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


from vas.gemfire.Groups import Group
from vas.gemfire.Installations import Installation
from vas.gemfire.CacheServerInstances import CacheServerInstances, CacheServerInstance
from vas.gemfire.CacheServerLiveConfigurations import CacheServerLiveConfigurations
from vas.gemfire.CacheServerNodeInstances import CacheServerNodeInstance
from vas.gemfire.CacheServerPendingConfigurations import CacheServerPendingConfigurations
from vas.gemfire.LiveApplicationCodes import LiveApplicationCodes
from vas.gemfire.PendingApplicationCodes import PendingApplicationCodes
from vas.test.VasTestCase import VasTestCase

class TestCacheServerInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            CacheServerInstances(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/'))

    def test_create(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/'
        self._return_location('https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/')

        instance = CacheServerInstances(self._client, location).create(
            Installation(self._client, installation_location),
            'example')

        self.assertIsInstance(instance, CacheServerInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location}, 'cache-server-group-instance')

    def test_detail(self):
        self._assert_item(
            CacheServerInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'), [
                ('name', 'example'),
                ('state', 'STOPPED'),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('live_application_code', lambda actual: self.assertIsInstance(actual, LiveApplicationCodes)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, CacheServerLiveConfigurations)),
                ('node_instances', [
                    CacheServerNodeInstance(self._client,
                        'https://localhost:8443/gemfire/v1/nodes/1/cache-server-instances/6/'),
                    CacheServerNodeInstance(self._client,
                        'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/5/')
                ]),
                ('pending_application_code', lambda actual: self.assertIsInstance(actual, PendingApplicationCodes)),
                ('pending_configurations',
                 lambda actual: self.assertIsInstance(actual, CacheServerPendingConfigurations))
            ])

    def test_start_parallel(self):
        CacheServerInstance(self._client,
            'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/').start()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        CacheServerInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/').start(
            True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        CacheServerInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/').stop()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        CacheServerInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/').stop(
            True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'

        CacheServerInstance(self._client, location).update(Installation(self._client, installation_location))

        self._assert_post(location, {'installation': installation_location})

    def test_delete(self):
        self._assert_deletable(
            CacheServerInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'))
