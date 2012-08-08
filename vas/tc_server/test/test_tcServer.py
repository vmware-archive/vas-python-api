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
from vas.tc_server.TcServerInstallationImages import TcServerInstallationImages
from vas.tc_server.TcServerRevisionImages import TcServerRevisionImages
from vas.tc_server.TcServer import TcServer
from vas.tc_server.TcServerGroups import TcServerGroups
from vas.tc_server.TcServerNodes import TcServerNodes
from vas.tc_server.TcServerTemplateImages import TcServerTemplateImages
from vas.test.StubClient import StubClient

class TestTcServer(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__tc_server = TcServer(self.__client, 'https://localhost:8443{}')

    def test_attributes(self):
        self.assertIsInstance(self.__tc_server.groups, TcServerGroups)
        self.assertIsInstance(self.__tc_server.installation_images, TcServerInstallationImages)
        self.assertIsInstance(self.__tc_server.nodes, TcServerNodes)
        self.assertIsInstance(self.__tc_server.revision_images, TcServerRevisionImages)
        self.assertIsInstance(self.__tc_server.template_images, TcServerTemplateImages)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__tc_server)),
            '__repr__ method has not been specified')
        eval(repr(self.__tc_server))
