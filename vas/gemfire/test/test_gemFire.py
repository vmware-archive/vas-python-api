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
from vas.gemfire.GemFireApplicationCodeImages import GemFireApplicationCodeImages
from vas.gemfire.GemFireInstallationImages import GemFireInstallationImages
from vas.gemfire.GemFire import GemFire
from vas.gemfire.GemFireGroups import GemFireGroups
from vas.gemfire.GemFireNodes import GemFireNodes
from vas.test.StubClient import StubClient

class TestGemFire(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__gemFire = GemFire(self.__client, 'https://localhost:8443{}')

    def test_attributes(self):
        self.assertIsInstance(self.__gemFire.application_code_images, GemFireApplicationCodeImages)
        self.assertIsInstance(self.__gemFire.groups, GemFireGroups)
        self.assertIsInstance(self.__gemFire.installation_images, GemFireInstallationImages)
        self.assertIsInstance(self.__gemFire.nodes, GemFireNodes)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__gemFire)),
            '__repr__ method has not been specified')
        eval(repr(self.__gemFire))
