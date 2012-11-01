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


from vas.rabbitmq.Groups import Group
from vas.rabbitmq.Installations import Installation
from vas.rabbitmq.Instances import Instances, Instance
from vas.rabbitmq.LiveConfigurations import LiveConfigurations
from vas.rabbitmq.NodeInstances import NodeInstance
from vas.rabbitmq.PendingConfigurations import PendingConfigurations
from vas.rabbitmq.Plugins import Plugins
from vas.test.VasTestCase import VasTestCase

class TestInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(Instances(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/'))

    def test_create(self):
        installation_location = 'https://localhost:8443/rabbitmq/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/rabbitmq/v1/groups/2/instances/'
        self._return_location('https://localhost:8443/rabbitmq/v1/groups/2/instances/4/')

        instance = Instances(self._client, location).create('example',
            Installation(self._client, installation_location))

        self.assertIsInstance(instance, Instance)
        self._assert_post(location, {'name': 'example', 'installation': installation_location}, 'group-instance')

    def test_detail(self):
        self._assert_item(Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/'), [
            ('name', 'example'),
            ('state', 'STOPPED'),
            ('group', lambda actual: self.assertIsInstance(actual, Group)),
            ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
            ('live_configurations', lambda actual: self.assertIsInstance(actual, LiveConfigurations)),
            ('node_instances', [NodeInstance(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/5/'),
                                NodeInstance(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/1/instances/6/')]),
            ('pending_configurations', lambda actual: self.assertIsInstance(actual, PendingConfigurations)),
            ('plugins', lambda actual: self.assertIsInstance(actual, Plugins))
        ])

    def test_delete(self):
        self._assert_deletable(Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/'))

    def test_start_parallel(self):
        Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/').start()
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/2/instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/').start(True)
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/2/instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/').stop()
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/2/instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        Instance(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/').stop(True)
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/2/instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update(self):
        installation_location = 'https://localhost:8443/rabbitmq/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/rabbitmq/v1/groups/2/instances/4/'

        Instance(self._client, location).update(Installation(self._client, installation_location))

        self._assert_post(location, {'installation', installation_location})
