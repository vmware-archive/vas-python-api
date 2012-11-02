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
from vas.test.VasTestCase import VasTestCase

class TestSecurity(VasTestCase):
    def test_security(self):
        self._assert_item(Security(self._client, 'https://localhost:8443/vfabric/v1/security/0/'), [
            ('owner', 'owner'),
            ('group', 'group'),
            ('permissions', {'owner': ['READ', 'WRITE', 'EXECUTE'], 'group': ['READ', 'WRITE'], 'other': ['READ']})
        ], False)

    def test_chown_no_optionals(self):
        Security(self._client, 'https://localhost:8443/vfabric/v1/security/0/').chown()
        self._assert_post('https://localhost:8443/vfabric/v1/security/0/', {})

    def test_chown_all_optionals(self):
        Security(self._client, 'https://localhost:8443/vfabric/v1/security/0/').chown(owner='owner-2', group='group-2')
        self._assert_post('https://localhost:8443/vfabric/v1/security/0/', {'owner': 'owner-2', 'group': 'group-2'})

    def test_chmod_no_optionals(self):
        Security(self._client, 'https://localhost:8443/vfabric/v1/security/0/').chmod()
        self._assert_post('https://localhost:8443/vfabric/v1/security/0/', {'permissions': {}})

    def test_chmod_all_optionals(self):
        Security(self._client, 'https://localhost:8443/vfabric/v1/security/0/').chmod(owner=['READ', 'WRITE'],
            group=['READ'], other=['READ', 'WRITE', 'EXECUTE'])
        self._assert_post('https://localhost:8443/vfabric/v1/security/0/',
            {'permissions': {'owner': ['READ', 'WRITE'], 'group': ['READ'], 'other': ['READ', 'WRITE', 'EXECUTE']}})
