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
from vas.gemfire.LocatorInstances import LocatorInstances, LocatorInstance
from vas.gemfire.LocatorLiveConfigurations import LocatorLiveConfigurations
from vas.gemfire.LocatorNodeInstances import LocatorNodeInstance
from vas.gemfire.LocatorPendingConfigurations import LocatorPendingConfigurations
from vas.test.VasTestCase import VasTestCase

class TestLocatorInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            LocatorInstances(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/'))

    def test_create(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/gemfire/v1/groups/0/locator-instances/'
        self._return_location('https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/')

        instance = LocatorInstances(self._client, location).create(Installation(self._client, installation_location),
            'example', 'test-address', True, 12345, False)

        self.assertIsInstance(instance, LocatorInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location, 'address': 'test-address', 'peer': True,
             'port': 12345, 'server': False}, 'locator-group-instance')

    def test_detail(self):
        self._assert_item(
            LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/'), [
                ('name', 'example'),
                ('address', 'host.example.com'),
                ('peer', lambda actual: self.assertTrue(actual)),
                ('port', 42222),
                ('server', lambda actual: self.assertTrue(actual)),
                ('state', 'STOPPED'),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, LocatorLiveConfigurations)),
                ('node_instances', [
                    LocatorNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/1/locator-instances/6/'),
                    LocatorNodeInstance(self._client, 'https://localhost:8443/gemfire/v1/nodes/0/locator-instances/5/')
                ]),
                ('pending_configurations', lambda actual: self.assertIsInstance(actual, LocatorPendingConfigurations))
            ])

    def test_start_parallel(self):
        LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/').start()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/').start(True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/').stop()
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/').stop(True)
        self._assert_post('https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update(self):
        installation_location = 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/'

        LocatorInstance(self._client, location).update(Installation(self._client, installation_location),
            'test-address', True, 12345, False)

        self._assert_post(location,
            {'installation': installation_location, 'address': 'test-address', 'peer': True, 'port': 12345,
             'server': False})

    def test_delete(self):
        self._assert_deletable(
            LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/2/locator-instances/4/'))
