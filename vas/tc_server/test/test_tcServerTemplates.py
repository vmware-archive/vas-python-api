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
from vas.tc_server.TcServerTemplate import TcServerTemplate
from vas.tc_server.TcServerTemplateImage import TcServerTemplateImage
from vas.tc_server.TcServerTemplates import TcServerTemplates
from vas.test.StubClient import StubClient

class TestTcServerTemplates(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__templates = TcServerTemplates(self.__client,
            'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/')

    def test_delete(self):
        self.__templates.delete(
            TcServerTemplate(self.__client,
                'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'

        revision = self.__templates.create(
            TcServerTemplateImage(self.__client, 'https://localhost:8443/tc-server/v1/template-images/0/'))

        self.assertIsInstance(revision, TcServerTemplate)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/',
                {'image': 'https://localhost:8443/tc-server/v1/template-images/0/'}, 'template')

    def test_attributes(self):
        self.assertIsInstance(self.__templates.security, Security)

    def test__create_item(self):
        self.assertIsInstance(self.__templates._create_item(self.__client,
            'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'), TcServerTemplate)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__templates:
            count += 1

        self.assertEqual(3, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__templates)),
            '__repr__ method has not been specified')
        eval(repr(self.__templates))
