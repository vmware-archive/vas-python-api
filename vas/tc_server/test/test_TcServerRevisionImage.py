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
from vas.tc_server.TcServerGroupRevision import TcServerGroupRevision
from vas.tc_server.TcServerRevisionImage import TcServerRevisionImage
from vas.test.StubClient import StubClient

class TestTcServerRevisionImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__revision_image = TcServerRevisionImage(self.__client,
            'https://localhost:8443/tc-server/v1/revision-images/0/')

    def test_attributes(self):
        self.assertEqual('example', self.__revision_image.name)
        self.assertEquals(5673284, self.__revision_image.size)
        self.assertEqual('1.0.0', self.__revision_image.version)
        self.assertEqual(
            [TcServerGroupRevision(self.__client,
                'https://localhost:8443/tc-server/v1/groups/5/instances/6/applications/7/revisions/8/'),
             TcServerGroupRevision(self.__client,
                 'https://localhost:8443/tc-server/v1/groups/1/instances/2/applications/3/revisions/4/')],
            self.__revision_image.revisions)
        self.assertIsInstance(self.__revision_image.security, Security)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__revision_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__revision_image))
