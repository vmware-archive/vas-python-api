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
from vas.test.StubClient import StubClient

class TestSecurity(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__security = Security(self.__client, 'https://localhost:8443/vfabric/v1/security/0/')

    def test_attributes(self):
        self.assertEqual('owner', self.__security.owner)
        self.assertEqual('group', self.__security.group)
        self.assertEqual({'owner': ['READ', 'WRITE', 'EXECUTE'], 'group': ['READ', 'WRITE'], 'other': ['READ']},
            self.__security.permissions)

    def test_chown_no_optionals(self):
        self.__client.delegate.reset_mock()
        self.__security.chown()
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/vfabric/v1/security/0/', {})
        self.assertEqual('owner', self.__security.owner)
        self.assertEqual('group', self.__security.group)

    def test_chown_all_optionals(self):
        self.__client.delegate.reset_mock()
        self.__security.chown(owner='owner-2', group='group-2')
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/vfabric/v1/security/0/',
                {'owner': 'owner-2', 'group': 'group-2'})
        self.assertEqual('owner-2', self.__security.owner)
        self.assertEqual('group-2', self.__security.group)

    def test_chmod_no_optionals(self):
        self.__client.delegate.reset_mock()
        self.__security.chmod()
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/vfabric/v1/security/0/',
                {'permissions': {}})
        self.assertEqual({'owner': ['READ', 'WRITE', 'EXECUTE'], 'group': ['READ', 'WRITE'], 'other': ['READ']},
            self.__security.permissions)

    def test_chmod_all_optionals(self):
        self.__client.delegate.reset_mock()
        self.__security.chmod(owner=['READ', 'WRITE'], group=['READ'], other=['READ', 'WRITE', 'EXECUTE'])
        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/vfabric/v1/security/0/',
                {'permissions': {'owner': ['READ', 'WRITE'], 'group': ['READ'], 'other': ['READ', 'WRITE', 'EXECUTE']}})
        self.assertEqual({'owner': ['READ', 'WRITE'], 'group': ['READ'], 'other': ['READ', 'WRITE', 'EXECUTE']},
            self.__security.permissions)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__security)),
            '__repr__ method has not been specified')
        eval(repr(self.__security))
