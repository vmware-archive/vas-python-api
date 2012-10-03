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
from datetime import datetime
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.gemfire.GemFireCacheServerLog import GemFireCacheServerLog
from vas.gemfire.GemFireCacheServerNodeInstance import GemFireCacheServerNodeInstance
from vas.test.StubClient import StubClient

class TestGemFireCacheServerLog(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__log = GemFireCacheServerLog(self.__client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/logs/4/')

    def test_attributes(self):
        self.assertEqual(datetime(2012, 5, 24, 15, 20, 56), self.__log.last_modified)
        self.assertEqual('example.log', self.__log.name)
        self.assertEqual(17638, self.__log.size)
        self.assertIsInstance(self.__log.instance, GemFireCacheServerNodeInstance)
        self.assertIsInstance(self.__log.security, Security)

    def test_content(self):
        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-cache-server-instances-logs-content\n', self.__log.content())
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/logs/4/content/')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-cache-server-instances-logs-content\n', self.__log.content(start_line='1'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/logs/4/content/?start-line=1')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-cache-server-instances-logs-content\n', self.__log.content(end_line='2'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/logs/4/content/?end-line=2')

        self.__client.delegate.reset_mock()
        self.assertEqual('nodes-cache-server-instances-logs-content\n',
            self.__log.content(start_line='1', end_line='2'))
        self.__client.delegate.get.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/logs/4/content/?start-line=1&end-line=2')

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__log)), '__repr__ method has not been specified')
        eval(repr(self.__log))
