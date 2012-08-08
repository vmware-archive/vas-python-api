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
from vas.rabbitmq.RabbitMqInstallationImages import RabbitMqInstallationImages
from vas.rabbitmq.RabbitMqPluginImages import RabbitMqPluginImages
from vas.rabbitmq.RabbitMq import RabbitMq
from vas.rabbitmq.RabbitMqGroups import RabbitMqGroups
from vas.rabbitmq.RabbitMqNodes import RabbitMqNodes
from vas.test.StubClient import StubClient

class TestRabbitMq(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__rabbitMq = RabbitMq(self.__client, 'https://localhost:8443{}')

    def test_attributes(self):
        self.assertIsInstance(self.__rabbitMq.groups, RabbitMqGroups)
        self.assertIsInstance(self.__rabbitMq.installation_images, RabbitMqInstallationImages)
        self.assertIsInstance(self.__rabbitMq.nodes, RabbitMqNodes)
        self.assertIsInstance(self.__rabbitMq.plugin_images, RabbitMqPluginImages)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__rabbitMq)),
            '__repr__ method has not been specified')
        eval(repr(self.__rabbitMq))
