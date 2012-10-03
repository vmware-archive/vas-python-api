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
from vas.gemfire.GemFireAgentGroupInstance import GemFireAgentGroupInstance
from vas.gemfire.GemFireAgentLiveConfiguration import GemFireAgentLiveConfiguration
from vas.test.StubClient import StubClient

class TestGemFireAgentLiveConfiguration(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__configuration = GemFireAgentLiveConfiguration(self.__client,
            'https://localhost:8443/gemfire/v1/groups/0/agent-instances/1/configurations/live/2/')

    def test_attributes(self):
        self.assertEqual('agent.properties', self.__configuration.path)
        self.assertEqual(10537, self.__configuration.size)
        self.assertEqual('groups-agent-instances-configurations-live-content\n', self.__configuration.content)
        self.assertIsInstance(self.__configuration.instance, GemFireAgentGroupInstance)
        self.assertIsInstance(self.__configuration.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__configuration)),
            '__repr__ method has not been specified')
        eval(repr(self.__configuration))
