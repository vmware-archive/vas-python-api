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


from vas.sqlfire.Groups import Group
from vas.sqlfire.Installations import Installation
from vas.sqlfire.LocatorInstances import LocatorInstances, LocatorInstance
from vas.sqlfire.LocatorLiveConfigurations import LocatorLiveConfigurations
from vas.sqlfire.LocatorNodeInstances import LocatorNodeInstance
from vas.sqlfire.LocatorPendingConfigurations import LocatorPendingConfigurations
from vas.test.VasTestCase import VasTestCase

class TestLocatorInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(
            LocatorInstances(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/'))

    def test_create_no_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/'
        self._return_location('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/')

        instance = LocatorInstances(self._client, location).create(Installation(self._client, installation_location),
            'example')

        self.assertIsInstance(instance, LocatorInstance)
        self._assert_post(location, {'name': 'example', 'installation': installation_location},
            'locator-group-instance')

    def test_create_all_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/'
        self._return_location('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/')

        instance = LocatorInstances(self._client, location).create(Installation(self._client, installation_location),
            'example', 'bind.address', 'client.bind.address', 1234, '256M', ['-Da=alpha'], '512M',
            'peer.discovery.address', 2345, True)

        self.assertIsInstance(instance, LocatorInstance)
        self._assert_post(location,
            {'name': 'example', 'installation': installation_location, 'bind-address': 'bind.address',
             'client-bind-address': 'client.bind.address', 'client-port': 1234, 'initial-heap': '256M',
             'jvm-options': ['-Da=alpha'], 'max-heap': '512M', 'peer-discovery-address': 'peer.discovery.address',
             'peer-discovery-port': 2345, 'run-netserver': True}, 'locator-group-instance')

    def test_detail(self):
        self._assert_item(
            LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/'), [
                ('bind_address', 'bind.address'),
                ('client_bind_address', 'client.bind.address'),
                ('client_port', 1234),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('initial_heap', '256M'),
                ('jvm_options', ['-Da=alpha']),
                ('live_configurations', lambda actual: self.assertIsInstance(actual, LocatorLiveConfigurations)),
                ('max_heap', '512M'),
                ('name', 'example'),
                ('node_instances', [
                    LocatorNodeInstance(self._client, 'https://localhost:8443/sqlfire/v1/nodes/1/locator-instances/6/'),
                    LocatorNodeInstance(self._client, 'https://localhost:8443/sqlfire/v1/nodes/0/locator-instances/5/')
                ]),
                ('peer_discovery_address', 'peer.discovery.address'),
                ('peer_discovery_port', 2345),
                ('pending_configurations', lambda actual: self.assertIsInstance(actual, LocatorPendingConfigurations)),
                ('run_netserver', lambda actual: self.assertTrue(actual)),
                ('state', 'STOPPED')
            ])

    def test_start_parallel(self):
        LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/').start()
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/').start(True)
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/').stop()
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/').stop(True)
        self._assert_post('https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update_no_optionals(self):
        location = 'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/4/'

        LocatorInstance(self._client, location).update()

        self._assert_post(location, {})

    def test_update_all_optionals(self):
        installation_location = 'https://localhost:8443/sqlfire/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/sqlfire/v1/groups/0/locator-instances/4/'

        LocatorInstance(self._client, location).update(Installation(self._client, installation_location),
            'bind.address', 'client.bind.address', 1234, '256M', ['-Da=alpha'], '512M', 'peer.discovery.address', 2345,
            True)

        self._assert_post(location,
            {'installation': installation_location, 'bind-address': 'bind.address',
             'client-bind-address': 'client.bind.address', 'client-port': 1234, 'initial-heap': '256M',
             'jvm-options': ['-Da=alpha'], 'max-heap': '512M', 'peer-discovery-address': 'peer.discovery.address',
             'peer-discovery-port': 2345, 'run-netserver': True})

    def test_delete(self):
        self._assert_deletable(
            LocatorInstance(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/locator-instances/4/'))
