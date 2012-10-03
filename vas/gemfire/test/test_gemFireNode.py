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
from vas.gemfire.GemFireNode import GemFireNode
from vas.gemfire.GemFireAgentNodeInstances import GemFireAgentNodeInstances
from vas.gemfire.GemFireCacheServerNodeInstances import GemFireCacheServerNodeInstances
from vas.gemfire.GemFireLocatorNodeInstances import GemFireLocatorNodeInstances
from vas.test.StubClient import StubClient

class TestGemFireNode(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__node = GemFireNode(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/')

    def test_attributes(self):
        self.assertEqual('/opt/vmware/vfabric-administration-agent', self.__node.agent_home)
        self.assertEqual('x64', self.__node.architecture)
        self.assertEqual([GemFireGroup(self.__client, 'https://localhost:8443/gemfire/v1/groups/2/'),
                          GemFireGroup(self.__client, 'https://localhost:8443/gemfire/v1/groups/1/')],
            self.__node.groups)
        self.assertEqual(['example-host'], self.__node.host_names)
        self.assertEqual(['192.168.0.2', '127.0.0.1'], self.__node.ip_addresses)
        self.assertEqual('usr/bin', self.__node.java_home)
        self.assertEqual({'a': 'alpha', 'b': 'bravo'}, self.__node.metadata)
        self.assertIsInstance(self.__node.agent_instances, GemFireAgentNodeInstances)
        self.assertIsInstance(self.__node.cache_server_instances, GemFireCacheServerNodeInstances)
        self.assertIsInstance(self.__node.locator_instances, GemFireLocatorNodeInstances)
        self.assertEqual('Linux', self.__node.operating_system)
        self.assertIsInstance(self.__node.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__node)), '__repr__ method has not been specified')
        eval(repr(self.__node))

