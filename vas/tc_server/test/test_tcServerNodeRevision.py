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
from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
from vas.tc_server.TcServerNodeRevision import TcServerNodeRevision
from vas.test.StubClient import StubClient

class TestTcServerNodeRevision(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__revision = TcServerNodeRevision(self.__client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/')

    def test_attributes(self):
        self.assertEqual('1.0.0', self.__revision.version)
        self.assertEqual('STOPPED', self.__revision.state)
        self.assertIsInstance(self.__revision.group_revision, TcServerGroupRevision)
        self.assertIsInstance(self.__revision.application, TcServerNodeApplication)
        self.assertIsInstance(self.__revision.security, Security)

    def test_start(self):
        self.__revision.start()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/state/',
                {'status': 'STARTED'})

    def test_stop(self):
        self.__revision.stop()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/state/',
                {'status': 'STOPPED'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__revision)),
            '__repr__ method has not been specified')
        eval(repr(self.__revision))

