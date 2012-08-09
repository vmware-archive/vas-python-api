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
from vas.gemfire.GemFireApplicationCodeImage import GemFireApplicationCodeImage
from vas.shared.Security import Security
from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFirePendingApplicationCode import GemFirePendingApplicationCode
from vas.test.StubClient import StubClient

class TestGemFirePendingApplicationCode(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__pending_application_code = GemFirePendingApplicationCode(self.__client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/')

    def test_attributes(self):
        self.assertEqual('example', self.__pending_application_code.name)
        self.assertEqual('1.0.0', self.__pending_application_code.version)
        self.assertIsInstance(self.__pending_application_code.application_code_image, GemFireApplicationCodeImage)
        self.assertIsInstance(self.__pending_application_code.instance, GemFireCacheServerGroupInstance)
        self.assertIsInstance(self.__pending_application_code.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__pending_application_code)),
            '__repr__ method has not been specified')
        eval(repr(self.__pending_application_code))
