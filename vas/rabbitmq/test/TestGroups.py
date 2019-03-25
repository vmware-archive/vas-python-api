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


from vas.rabbitmq.Groups import Groups, Group
from vas.rabbitmq.Installations import Installations
from vas.rabbitmq.Instances import Instances
from vas.rabbitmq.Nodes import Node
from vas.test.VasTestCase import VasTestCase

class TestGroups(VasTestCase):
    def test_list(self):
        self._assert_collection(Groups(self._client, 'https://localhost:8443/rabbitmq/v1/groups/'))

    def test_create(self):
        node_location_0 = 'https://localhost:8443/rabbitmq/v1/nodes/0/'
        node_location_1 = 'https://localhost:8443/rabbitmq/v1/nodes/1/'
        location = 'https://localhost:8443/rabbitmq/v1/groups/'
        self._return_location('https://localhost:8443/rabbitmq/v1/groups/2/')

        group = Groups(self._client, location).create('example-group',
            [Node(self._client, node_location_0), Node(self._client, node_location_1)])

        self.assertIsInstance(group, Group)
        self._assert_post(location, {'name': 'example-group', 'nodes': [node_location_0, node_location_1]}, 'group')

    def test_detail(self):
        self._assert_item(Group(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/'), [
            ('name', 'example-group'),
            ('instances', lambda actual: self.assertIsInstance(actual, Instances)),
            ('installations', lambda actual: self.assertIsInstance(actual, Installations)),
            ('nodes', [Node(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/1/'),
                       Node(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/')])
        ])

    def test_delete(self):
        self._assert_deletable(Group(self._client, 'https://localhost:8443/rabbitmq/v1/groups/2/'))
