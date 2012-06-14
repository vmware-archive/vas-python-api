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


from vas.shared.Security import Security
from vas.test.test_TestRoot import TestRoot

class TestSecurity(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['security-href'] = {
        'owner': 'owner',
        'group': 'group',
        'permissions': {
            'owner': ['READ', 'WRITE', 'EXECUTE'],
            'group': ['READ', 'WRITE'],
            'other': ['EXECUTE']
        }
    }

    _PAYLOADS['less-than-href'] = {
        'owner': 'owner',
        'group': 'group',
        'permissions': {
            'owner': ['READ', 'WRITE', 'EXECUTE'],
            'group': ['READ', 'WRITE'],
            'other': ['EXECUTE']
        }
    }

    def setUp(self):
        super(TestSecurity, self).setUp()
        self.__security = Security(self._client, 'security-href')

    def test_attributes(self):
        self.assertEqual('owner', self.__security.owner)
        self.assertEqual('group', self.__security.group)
        self.assertEqual({'owner': ['READ', 'WRITE', 'EXECUTE'], 'group': ['READ', 'WRITE'], 'other': ['EXECUTE']},
                                                                                                                  self.__security.permissions)

    def test_update(self):
        self.__security.update()
        self._client.post.assert_called_with('security-href', {})

        self.__security.update(owner='owner-2')
        self._client.post.assert_called_with('security-href', {'owner': 'owner-2'})

        self.__security.update(group='group-2')
        self._client.post.assert_called_with('security-href', {'group': 'group-2'})

        self.__security.update(permissions={'other': ['EXECUTE']})
        self._client.post.assert_called_with('security-href', {'permissions': {'other': ['EXECUTE']}})

    def test_equals(self):
        self.assertEqual(Security(self._client, 'security-href'), self.__security)

    def test_hash(self):
        self.assertEqual(hash(Security(self._client, 'security-href')), hash(self.__security))

    def test_less_than(self):
        security_less_than = Security(self._client, 'less-than-href')
        self.assertTrue(security_less_than < self.__security)
        self.assertFalse(security_less_than > self.__security)