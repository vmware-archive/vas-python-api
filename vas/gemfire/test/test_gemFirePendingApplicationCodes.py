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
from vas.gemfire.GemFirePendingApplicationCode import GemFirePendingApplicationCode
from vas.gemfire.GemFirePendingApplicationCodes import GemFirePendingApplicationCodes
from vas.test.StubClient import StubClient

class TestGemFirePendingApplicationCodes(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__pending_application_codes = GemFirePendingApplicationCodes(self.__client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/')

    def test_delete(self):
        self.__pending_application_codes.delete(
            GemFirePendingApplicationCode(self.__client,
                'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/2/application-code/pending/3/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/'

        pending_configuration = self.__pending_application_codes.create(
            GemFireApplicationCodeImage(self.__client, 'https://localhost:8443/gemfire/v1/application-code-images/0/'))

        self.assertIsInstance(pending_configuration, GemFirePendingApplicationCode)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/',
            {'image': 'https://localhost:8443/gemfire/v1/application-code-images/0/'})

    def test_attributes(self):
        self.assertIsInstance(self.__pending_application_codes.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__pending_application_codes._create_item(self.__client,
                'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/'),
            GemFirePendingApplicationCode)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__pending_application_codes:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__pending_application_codes)),
            '__repr__ method has not been specified')
        eval(repr(self.__pending_application_codes))
