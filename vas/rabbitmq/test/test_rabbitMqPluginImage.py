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
from vas.shared.Security import Security
from vas.rabbitmq.RabbitMqGroupPlugin import RabbitMqGroupPlugin
from vas.rabbitmq.RabbitMqPluginImage import RabbitMqPluginImage
from vas.test.StubClient import StubClient

class TestRabbitMqPluginImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__plugin_image = RabbitMqPluginImage(self.__client,
            'https://localhost:8443/rabbitmq/v1/plugin-images/0/')

    def test_attributes(self):
        self.assertEqual('example', self.__plugin_image.name)
        self.assertEquals(5673284, self.__plugin_image.size)
        self.assertEqual('1.0.0', self.__plugin_image.version)
        self.assertEqual(
            [RabbitMqGroupPlugin(self.__client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/5/'),
             RabbitMqGroupPlugin(self.__client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/4/')],
            self.__plugin_image.plugins)
        self.assertIsInstance(self.__plugin_image.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__plugin_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__plugin_image))


