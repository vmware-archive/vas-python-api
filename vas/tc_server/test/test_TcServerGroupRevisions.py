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
from vas.tc_server.TcServerGroupRevisions import TcServerGroupRevisions
from vas.test.StubClient import StubClient

class TestTcServerGroupRevisions(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__revisions = TcServerGroupRevisions(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/')

    def test_delete(self):
        self.__revisions.delete(
            TcServerGroupRevision(self.__client,
                'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/')

    def test_create(self):
        self.__client.delegate.post.return_value = 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/5/'

        revision = self.__revisions.create(
            TcServerRevisionImage(self.__client, 'https://localhost:8443/tc-server/v1/revision-images/0/'))

        self.assertIsInstance(revision, TcServerGroupRevision)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/',
                {'image': 'https://localhost:8443/tc-server/v1/revision-images/0/'}, 'group-revision')

    def test_attributes(self):
        self.assertIsInstance(self.__revisions.security, Security)

    def test__create_item(self):
        self.assertIsInstance(self.__revisions._create_item(self.__client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/5/'),
            TcServerGroupRevision)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__revisions:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__revisions)),
            '__repr__ method has not been specified')
        eval(repr(self.__revisions))
