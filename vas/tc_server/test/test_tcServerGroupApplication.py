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
from vas.tc_server.TcServerGroupApplication import TcServerGroupApplication
from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerGroupRevisions import TcServerGroupRevisions
from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
from vas.test.StubClient import StubClient

class TestTcServerGroupApplication(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__application = TcServerGroupApplication(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/')

    def test_attributes(self):
        self.assertEqual('/example', self.__application.context_path)
        self.assertEqual('localhost', self.__application.host)
        self.assertEqual('Example', self.__application.name)
        self.assertEqual('Catalina', self.__application.service)
        self.assertIsInstance(self.__application.instance, TcServerGroupInstance)
        self.assertIsInstance(self.__application.revisions, TcServerGroupRevisions)
        self.assertEqual(
            [TcServerNodeApplication(self.__client,
                'https://localhost:8443/tc-server/v1/nodes/1/instances/5/applications/8/'),
             TcServerNodeApplication(self.__client,
                 'https://localhost:8443/tc-server/v1/nodes/0/instances/4/applications/7/')],
            self.__application.node_applications)
        self.assertIsInstance(self.__application.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__application)),
            '__repr__ method has not been specified')
        eval(repr(self.__application))
