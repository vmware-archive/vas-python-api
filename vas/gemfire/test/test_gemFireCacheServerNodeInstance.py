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
from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFireCacheServerLogs import GemFireCacheServerLogs
from vas.gemfire.GemFireCacheServerNodeInstance import GemFireCacheServerNodeInstance
from vas.gemfire.GemFireDiskStores import GemFireDiskStores
from vas.gemfire.GemFireNode import GemFireNode
from vas.gemfire.GemFireStatistics import GemFireStatistics
from vas.test.StubClient import StubClient

class TestGemFireCacheServerNodeInstance(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instance = GemFireCacheServerNodeInstance(self.__client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/')

    def test_attributes(self):
        self.assertIsInstance(self.__instance.disk_stores, GemFireDiskStores)
        self.assertIsInstance(self.__instance.group_instance, GemFireCacheServerGroupInstance)
        self.assertIsInstance(self.__instance.logs, GemFireCacheServerLogs)
        self.assertEqual('example', self.__instance.name)
        self.assertIsInstance(self.__instance.node, GemFireNode)
        self.assertEqual('STOPPED', self.__instance.state)
        self.assertIsInstance(self.__instance.statistics, GemFireStatistics)
        self.assertIsInstance(self.__instance.security, Security)

    def test_start_rebalanced(self):
        self.__instance.start(True)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/state/',
            {'status': 'STARTED', 'rebalance': True})

    def test_start_not_rebalanced(self):
        self.__instance.start(False)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/state/',
            {'status': 'STARTED', 'rebalance': False})


    def test_stop(self):
        self.__instance.stop()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/state/', {'status': 'STOPPED'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instance)),
            '__repr__ method has not been specified')
        eval(repr(self.__instance))
