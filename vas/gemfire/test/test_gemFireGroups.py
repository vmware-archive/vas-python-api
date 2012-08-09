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
from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireGroups import GemFireGroups
from vas.gemfire.GemFireNode import GemFireNode
from vas.test.StubClient import StubClient

class TestGemFireGroups(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__groups = GemFireGroups(self.__client, 'https://localhost:8443/gemfire/v1/groups/')

    def test_delete(self):
        self.__groups.delete(GemFireGroup(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/'))
        self.__client.delegate.delete.assert_called_once_with('https://localhost:8443/gemfire/v1/groups/2/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/gemfire/v1/groups/2/'

        group = self.__groups.create('example-group',
            [GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/'),
             GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/1/')])

        self.assertIsInstance(group, GemFireGroup)
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/gemfire/v1/groups/',
                {'name': 'example-group', 'nodes': ['https://localhost:8443/gemfire/v1/nodes/0/',
                                                    'https://localhost:8443/gemfire/v1/nodes/0/']}, 'group')

    def test_attributes(self):
        self.assertIsInstance(self.__groups.security, Security)

    def test__create_item(self):
        self.assertIsInstance(self.__groups._create_item(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/'),
            GemFireGroup)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__groups:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__groups)),
            '__repr__ method has not been specified')
        eval(repr(self.__groups))
