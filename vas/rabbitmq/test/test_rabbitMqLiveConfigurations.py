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
from vas.rabbitmq.RabbitMqLiveConfiguration import RabbitMqLiveConfiguration
from vas.rabbitmq.RabbitMqLiveConfigurations import RabbitMqLiveConfigurations
from vas.test.StubClient import StubClient

class TestRabbitMqLiveConfigurations(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__live_configurations = RabbitMqLiveConfigurations(self.__client,
            'https://localhost:8443/rabbitmq/v1/groups/0/instances/1/configurations/live/')

    def test_attributes(self):
        self.assertIsInstance(self.__live_configurations.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__live_configurations._create_item(self.__client,
                'https://localhost:8443/rabbitmq/v1/groups/0/instances/1/configurations/live/2/'),
            RabbitMqLiveConfiguration)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__live_configurations:
            count += 1

        self.assertEqual(1, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__live_configurations)),
            '__repr__ method has not been specified')
        eval(repr(self.__live_configurations))
