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
from vas.tc_server.TcServerInstallation import TcServerInstallation
from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerGroupInstances import TcServerGroupInstances
from vas.tc_server.TcServerTemplate import TcServerTemplate
from vas.test.StubClient import StubClient

class TestTcServerGroupInstances(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instances = TcServerGroupInstances(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/')

    def test_delete(self):
        self.__instances.delete(
            TcServerGroupInstance(self.__client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/2/instances/4/')

    def test_create_no_optionals(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'

        instance = self.__instances.create('example',
            TcServerInstallation(self.__client, 'https://localhost:8443/tc-server/v1/groups/2/installations/3/'))

        self.assertIsInstance(instance, TcServerGroupInstance)
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/tc-server/v1/groups/0/instances/',
                {'name': 'example', 'installation': 'https://localhost:8443/tc-server/v1/groups/1/installations/2/'},
            'group-instance')

    def test_create_all_optionals(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'

        instance = self.__instances.create('example',
            TcServerInstallation(self.__client, 'https://localhost:8443/tc-server/v1/groups/2/installations/3/'),
            layout='SEPARATE', properties={'a': 'alpha', 'b': 'bravo'}, runtime_version='7.0.21.A.RELEASE',
            templates=[TcServerTemplate(self.__client,
                'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'),
                       TcServerTemplate(self.__client,
                           'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')])

        self.assertIsInstance(instance, TcServerGroupInstance)
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/tc-server/v1/groups/0/instances/',
                {'name': 'example', 'installation': 'https://localhost:8443/tc-server/v1/groups/1/installations/2/',
                 'layout': 'SEPARATE', 'properties': {'a': 'alpha', 'b': 'bravo'},
                 'runtime-version': '7.0.21.A.RELEASE',
                 'templates': ['https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/',
                               'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/']},
            'group-instance')

    def test_attributes(self):
        self.assertIsInstance(self.__instances.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__instances._create_item(self.__client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'),
            TcServerGroupInstance)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__instances:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instances)),
            '__repr__ method has not been specified')
        eval(repr(self.__instances))
