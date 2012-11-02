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


from vas.sqlfire.AgentInstances import AgentInstances
from vas.sqlfire.ServerInstances import ServerInstances
from vas.sqlfire.Groups import Groups, Group
from vas.sqlfire.Installations import Installations
from vas.sqlfire.LocatorInstances import LocatorInstances
from vas.sqlfire.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestGroups(VasTestCase):
    def test_list(self):
        self._assert_collection(Groups(self._client, 'https://localhost:8443/sqlfire/v1/groups/'))

    def test_create(self):
        node_0_location = 'https://localhost:8443/sqlfire/v1/nodes/0/'
        node_1_location = 'https://localhost:8443/sqlfire/v1/nodes/1/'
        location = 'https://localhost:8443/sqlfire/v1/groups/'
        self._return_location('https://localhost:8443/sqlfire/v1/groups/2/')

        group = Groups(self._client, location).create('example-group', [
            Node(self._client, node_0_location),
            Node(self._client, node_1_location)
        ])

        self.assertIsInstance(group, Group)
        self._assert_post(location, {'name': 'example-group', 'nodes': [node_0_location, node_1_location]}, 'group')

    def test_detail(self):
        self._assert_item(Group(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/'), [
            ('name', 'example-group'),
            ('agent_instances', lambda actual: self.assertIsInstance(actual, AgentInstances)),
            ('installations', lambda actual: self.assertIsInstance(actual, Installations)),
            ('locator_instances', lambda actual: self.assertIsInstance(actual, LocatorInstances)),
            ('nodes', [
                Node(self._client, 'https://localhost:8443/sqlfire/v1/nodes/0/'),
                Node(self._client, 'https://localhost:8443/sqlfire/v1/nodes/1/')
            ]),
            ('server_instances', lambda actual: self.assertIsInstance(actual, ServerInstances))
        ])

    def test_update(self):
        node_0_location = 'https://localhost:8443/sqlfire/v1/nodes/0/'
        node_1_location = 'https://localhost:8443/sqlfire/v1/nodes/1/'
        node_2_location = 'https://localhost:8443/sqlfire/v1/nodes/2/'
        location = 'https://localhost:8443/sqlfire/v1/groups/2/'

        Group(self._client, location).update([
            Node(self._client, node_0_location),
            Node(self._client, node_1_location),
            Node(self._client, node_2_location)
        ])

        self._assert_post(location, {'nodes': [node_0_location, node_1_location, node_2_location]})


    def test_delete(self):
        self._assert_deletable(Group(self._client, 'https://localhost:8443/sqlfire/v1/groups/2/'))
