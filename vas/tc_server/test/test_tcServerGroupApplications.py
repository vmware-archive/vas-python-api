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
from vas.tc_server.TcServerGroupApplications import TcServerGroupApplications
from vas.test.StubClient import StubClient

class TestTcServerGroupApplications(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__applications = TcServerGroupApplications(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/')

    def test_delete(self):
        self.__applications.delete(TcServerGroupApplication(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/'

        application = self.__applications.create('/Example', 'localhost', 'Example', 'Catalina')

        self.assertIsInstance(application, TcServerGroupApplication)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/applications/',
                {'context-path': '/Example', 'host': 'localhost', 'name': 'Example', 'service': 'Catalina'},
            'group-application')

    def test_attributes(self):
        self.assertIsInstance(self.__applications.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__applications._create_item(self.__client,
                'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/'), TcServerGroupApplication)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__applications:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__applications)),
            '__repr__ method has not been specified')
        eval(repr(self.__applications))
