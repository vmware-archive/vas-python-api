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
from vas.gemfire.GemFireAgentGroupInstance import GemFireAgentGroupInstance
from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFireInstallation import GemFireInstallation
from vas.gemfire.GemFireInstallationImage import GemFireInstallationImage
from vas.gemfire.GemFireLocatorGroupInstance import GemFireLocatorGroupInstance
from vas.test.StubClient import StubClient

class TestGemFireInstallation(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__installation = GemFireInstallation(self.__client,
            'https://localhost:8443/gemfire/v1/groups/1/installations/2/')

    def test_attributes(self):
        self.assertEqual('6.6.1', self.__installation.version)
        self.assertIsInstance(self.__installation.group, GemFireGroup)
        self.assertEqual(
            [GemFireAgentGroupInstance(self.__client, 'https://localhost:8443/gemfire/v1/groups/1/agent-instances/3/')],
            self.__installation.agent_instances)
        self.assertEqual(
            [GemFireCacheServerGroupInstance(self.__client,
                'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/5/'),
             GemFireCacheServerGroupInstance(self.__client,
                 'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/6/'), ],
            self.__installation.cache_server_instances)
        self.assertIsInstance(self.__installation.installation_image, GemFireInstallationImage)
        self.assertEqual(
            [GemFireLocatorGroupInstance(self.__client,
                'https://localhost:8443/gemfire/v1/groups/1/locator-instances/4/'), ],
            self.__installation.locator_instances)
        self.assertIsInstance(self.__installation.security, Security)


def test_repr(self):
    self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__installation)),
        '__repr__ method has not been specified')
    eval(repr(self.__installation))


