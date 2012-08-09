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
from vas.gemfire.GemFireInstallationImage import GemFireInstallationImage
from vas.test.StubClient import StubClient

class TestInstallationImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__installation_image = GemFireInstallationImage(self.__client,
            'https://localhost:8443/gemfire/v1/installation-images/0/')

    def test_attributes(self):
        self.assertEqual(7340032, self.__installation_image.size)
        self.assertEqual('6.6.1', self.__installation_image.version)
        self.assertEqual(
            [GemFireInstallation(self.__client, 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'),
             GemFireInstallation(self.__client, 'https://localhost:8443/gemfire/v1/groups/3/installations/4/')],
            self.__installation_image.installations)
        self.assertIsInstance(self.__installation_image.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__installation_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__installation_image))
