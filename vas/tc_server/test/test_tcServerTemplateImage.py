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
from vas.test.StubClient import StubClient

class TestTcServerTemplateImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__template_image = TcServerTemplateImage(self.__client,
            'https://localhost:8443/tc-server/v1/template-images/0/')

    def test_attributes(self):
        self.assertEqual('example', self.__template_image.name)
        self.assertEquals(5673284, self.__template_image.size)
        self.assertEqual('1.0.0', self.__template_image.version)
        self.assertEqual(
            [TcServerTemplate(self.__client,
                'https://localhost:8443/tc-server/v1/groups/4/installations/5/templates/6/'),
             TcServerTemplate(self.__client,
                 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')],
            self.__template_image.templates)
        self.assertIsInstance(self.__template_image.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__template_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__template_image))


