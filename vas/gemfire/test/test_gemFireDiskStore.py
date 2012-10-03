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
from vas.gemfire.GemFireDiskStore import GemFireDiskStore
from vas.gemfire.GemFireCacheServerNodeInstance import GemFireCacheServerNodeInstance
from vas.test.StubClient import StubClient

class TestGemFireDiskStore(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__disk_store = GemFireDiskStore(self.__client,
            'https://localhost:8443/gemfire/v1/nodes/0/cache-server-instances/3/disk-stores/4/')

    def test_attributes(self):
        self.assertEqual(datetime(2012, 5, 24, 15, 20, 56), self.__disk_store.last_modified)
        self.assertEqual('example.gfs', self.__disk_store.name)
        self.assertEqual(17638, self.__disk_store.size)
        self.assertEqual('nodes-cache-server-instances-disk-stores-content\n', self.__disk_store.content)
        self.assertIsInstance(self.__disk_store.instance, GemFireCacheServerNodeInstance)
        self.assertIsInstance(self.__disk_store.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__disk_store)), '__repr__ method has not been specified')
        eval(repr(self.__disk_store))
