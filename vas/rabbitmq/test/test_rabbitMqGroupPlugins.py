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


import re
from unittest.case import TestCase
from vas.rabbitmq.RabbitMqPluginImage import RabbitMqPluginImage
from vas.shared.Security import Security
from vas.rabbitmq.RabbitMqGroupPlugin import RabbitMqGroupPlugin
from vas.rabbitmq.RabbitMqGroupPlugins import RabbitMqGroupPlugins
from vas.test.StubClient import StubClient

class TestRabbitMqGroupPlugins(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__plugins = RabbitMqGroupPlugins(self.__client,
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/')

    def test_delete(self):
        self.__plugins.delete(RabbitMqGroupPlugin(self.__client,
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/rabbitmq/v1/groups/2/instances/3/plugins/6/'

        plugin = self.__plugins.create(
            RabbitMqPluginImage(self.__client, 'https://localhost:8443/rabbitmq/v1/plugin-images/0/'))

        self.assertIsInstance(plugin, RabbitMqGroupPlugin)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/',
                {'image': 'https://localhost:8443/rabbitmq/v1/plugin-images/0/'}, 'plugin')

    def test_attributes(self):
        self.assertIsInstance(self.__plugins.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__plugins._create_item(self.__client,
                'https://localhost:8443/rabbitmq/v1/groups/2/instances/3/plugins/6/'), RabbitMqGroupPlugin)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__plugins:
            count += 1

        self.assertEqual(3, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__plugins)),
            '__repr__ method has not been specified')
        eval(repr(self.__plugins))
