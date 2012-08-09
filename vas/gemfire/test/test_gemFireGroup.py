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
from vas.gemfire.GemFireInstallations import GemFireInstallations
from vas.gemfire.GemFireAgentGroupInstances import GemFireAgentGroupInstances
from vas.gemfire.GemFireCacheServerGroupInstances import GemFireCacheServerGroupInstances
from vas.gemfire.GemFireLocatorGroupInstances import GemFireLocatorGroupInstances
from vas.gemfire.GemFireNode import GemFireNode
from vas.test.StubClient import StubClient

class TestGemFireGroup(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__group = GemFireGroup(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/')

    def test_attributes(self):
        self.assertEqual('example-group', self.__group.name)
        self.assertIsInstance(self.__group.agent_instances, GemFireAgentGroupInstances)
        self.assertIsInstance(self.__group.cache_server_instances, GemFireCacheServerGroupInstances)
        self.assertIsInstance(self.__group.installations, GemFireInstallations)
        self.assertIsInstance(self.__group.locator_instances, GemFireLocatorGroupInstances)
        self.assertEqual(
            [GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/1/'),
             GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/')], self.__group.nodes)
        self.assertIsInstance(self.__group.security, Security)

    def test_update(self):
        self.__client.delegate.reset_mock()
        self.__group.update([GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/'),
                             GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/1/'),
                             GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/2/')])

        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/gemfire/v1/groups/2/',
                {'nodes': ['https://localhost:8443/gemfire/v1/nodes/0/',
                           'https://localhost:8443/gemfire/v1/nodes/0/',
                           'https://localhost:8443/gemfire/v1/nodes/0/']})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__group)), '__repr__ method has not been specified')
        eval(repr(self.__group))
