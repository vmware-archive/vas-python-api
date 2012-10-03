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
from vas.gemfire.GemFireStatistic import GemFireStatistic
from vas.gemfire.GemFireCacheServerNodeInstance import GemFireCacheServerNodeInstance
from vas.test.StubClient import StubClient

class TestGemFireStatistic(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__statistic = GemFireStatistic(self.__client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/statistics/4/')

    def test_attributes(self):
        self.assertEqual(datetime(2012, 5, 24, 15, 20, 56), self.__statistic.last_modified)
        self.assertEqual('example.statistic', self.__statistic.path)
        self.assertEqual(17638, self.__statistic.size)
        self.assertEqual('nodes-cache-server-instances-statistics-content\n', self.__statistic.content)
        self.assertIsInstance(self.__statistic.instance, GemFireCacheServerNodeInstance)
        self.assertIsInstance(self.__statistic.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__statistic)), '__repr__ method has not been specified')
        eval(repr(self.__statistic))
