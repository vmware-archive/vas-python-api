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
from vas.tc_server.TcServerGroupRevision import TcServerGroupRevision
from vas.tc_server.TcServerNodeRevision import TcServerNodeRevision
from vas.tc_server.TcServerRevisionImage import TcServerRevisionImage
from vas.test.StubClient import StubClient

class TestTcServerGroupRevision(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__revision = TcServerGroupRevision(self.__client,
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/')

    def test_attributes(self):
        self.assertEqual('1.0.0', self.__revision.version)
        self.assertEqual('STOPPED', self.__revision.state)
        self.assertIsInstance(self.__revision.application, TcServerGroupApplication)
        self.assertIsInstance(self.__revision.revision_image, TcServerRevisionImage)
        self.assertEqual(
            [TcServerNodeRevision(self.__client,
                'https://localhost:8443/tc-server/v1/nodes/1/instances/6/applications/9/revisions/12/'),
             TcServerNodeRevision(self.__client,
                 'https://localhost:8443/tc-server/v1/nodes/0/instances/5/applications/8/revisions/11/')],
            self.__revision.node_revisions)
        self.assertIsInstance(self.__revision.security, Security)

    def test_start(self):
        self.__revision.start()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/state/',
                {'status': 'STARTED'})

    def test_stop(self):
        self.__revision.stop()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/state/',
                {'status': 'STOPPED'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__revision)),
            '__repr__ method has not been specified')
        eval(repr(self.__revision))
