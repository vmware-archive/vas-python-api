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
from vas.gemfire.GemFireInstallation import GemFireInstallation
from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFireCacheServerGroupInstances import GemFireCacheServerGroupInstances
from vas.test.StubClient import StubClient

class TestGemFireCacheServerGroupInstances(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instances = GemFireCacheServerGroupInstances(self.__client,
            'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/')

    def test_delete(self):
        self.__instances.delete(
            GemFireCacheServerGroupInstance(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'

        instance = self.__instances.create('example',
            GemFireInstallation(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/installations/3/'))

        self.assertIsInstance(instance, GemFireCacheServerGroupInstance)
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/',
                {'name': 'example', 'installation': 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'},
            'cache-server-group-instance')

    def test_attributes(self):
        self.assertIsInstance(self.__instances.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__instances._create_item(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/cache-server-instances/4/'),
            GemFireCacheServerGroupInstance)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__instances:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instances)),
            '__repr__ method has not been specified')
        eval(repr(self.__instances))
