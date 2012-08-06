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
from vas.tc_server.TcServerGroup import TcServerGroup
from vas.tc_server.TcServerInstallations import TcServerInstallations
from vas.tc_server.TcServerGroupInstances import TcServerGroupInstances
from vas.tc_server.TcServerNode import TcServerNode
from vas.test.StubClient import StubClient

class TestTcServerGroup(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__group = TcServerGroup(self.__client, 'https://localhost:8443/tc-server/v1/groups/2/')

    def test_attributes(self):
        self.assertEqual('example-group', self.__group.name)
        self.assertIsInstance(self.__group.instances, TcServerGroupInstances)
        self.assertIsInstance(self.__group.installations, TcServerInstallations)
        self.assertEqual(
            [TcServerNode(self.__client, 'https://localhost:8443/tc-server/v1/nodes/1/'),
             TcServerNode(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/')], self.__group.nodes)
        self.assertIsInstance(self.__group.security, Security)

    def test_update(self):
        self.__client.delegate.reset_mock()
        self.__group.update([TcServerNode(self.__client, 'https://localhost:8443/tc-server/v1/nodes/0/'),
                             TcServerNode(self.__client, 'https://localhost:8443/tc-server/v1/nodes/1/'),
                             TcServerNode(self.__client, 'https://localhost:8443/tc-server/v1/nodes/2/')])

        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/tc-server/v1/groups/2/',
                {'nodes': ['https://localhost:8443/tc-server/v1/nodes/0/',
                           'https://localhost:8443/tc-server/v1/nodes/0/',
                           'https://localhost:8443/tc-server/v1/nodes/0/']})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__group)), '__repr__ method has not been specified')
        eval(repr(self.__group))
