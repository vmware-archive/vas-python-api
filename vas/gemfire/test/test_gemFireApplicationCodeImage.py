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
from vas.gemfire.GemFireLiveApplicationCode import GemFireLiveApplicationCode
from vas.gemfire.GemFirePendingApplicationCode import GemFirePendingApplicationCode
from vas.gemfire.GemFireApplicationCodeImage import GemFireApplicationCodeImage
from vas.test.StubClient import StubClient

class TestGemFireApplicationCodeImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__application_code_image = GemFireApplicationCodeImage(self.__client,
            'https://localhost:8443/gemfire/v1/application-code-images/0/')

    def test_attributes(self):
        self.assertEqual('example', self.__application_code_image.name)
        self.assertEquals(5673284, self.__application_code_image.size)
        self.assertEqual('1.0.0', self.__application_code_image.version)
        self.assertEqual(
            [GemFireLiveApplicationCode(self.__client,
                'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/2/application-code/live/3/'),
             GemFireLiveApplicationCode(self.__client,
                 'https://localhost:8443/gemfire/v1/groups/4/cache-server-instances/5/application-code/live/6/')],
            self.__application_code_image.live_application_code)
        self.assertEqual(
            [GemFirePendingApplicationCode(self.__client,
                'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/2/application-code/pending/12/'),
             GemFirePendingApplicationCode(self.__client,
                 'https://localhost:8443/gemfire/v1/groups/4/cache-server-instances/5/application-code/pending/9/')],
            self.__application_code_image.pending_application_code)
        self.assertIsInstance(self.__application_code_image.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__application_code_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__application_code_image))


