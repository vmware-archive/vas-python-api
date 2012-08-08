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
from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
from vas.test.StubClient import StubClient

class TestRabbitMqGroupPlugin(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__plugin = RabbitMqGroupPlugin(self.__client,
            'https://localhost:8443/rabbitmq/v1/groups/2/instances/3/plugins/6/')

    def test_attributes(self):
        self.assertEqual('example', self.__plugin.name)
        self.assertEqual('1.0.0', self.__plugin.version)
        self.assertIsInstance(self.__plugin.instance, RabbitMqGroupInstance)
        self.assertIsInstance(self.__plugin.plugin_image, RabbitMqPluginImage)
        self.assertIsInstance(self.__plugin.security, Security)
        self.assertEqual('ENABLED', self.__plugin.state)

    def test_enable(self):
        self.__plugin.enable()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/state/', {'status': 'ENABLED'})

    def test_disable(self):
        self.__plugin.disable()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/state/', {'status': 'DISABLED'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__plugin)),
            '__repr__ method has not been specified')
        eval(repr(self.__plugin))
