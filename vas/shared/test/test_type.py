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
from vas.shared.Type import Type
from vas.test.test_TestRoot import TestRoot

class TestType(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['type-href'] = {
        'links': [{
            'rel': 'security',
            'href': 'security-href'
        }, {
            'rel': 'self',
            'href': 'self-href'
        }]
    }

    _PAYLOADS['type-less-than-href'] = {
        'links': [{
            'rel': 'security',
            'href': 'security-href'
        }, {
            'rel': 'self',
            'href': 'less-than-href'
        }]
    }

    _PAYLOADS['security-href'] = {
        'owner': 'owner',
        'group': 'group',
        'permissions': {
            'owner': ['READ', 'WRITE', 'EXECUTE'],
            'group': ['READ', 'WRITE'],
            'other': ['EXECUTE']
        }
    }

    def setUp(self):
        super(TestType, self).setUp()
        self.__type = Type(self._client, 'type-href')

    def test_equals(self):
        self.assertEqual(Type(self._client, 'type-href'), self.__type)

    def test_hash(self):
        self.assertEqual(hash(Type(self._client, 'type-href')), hash(self.__type))

    def test_less_than(self):
        type_less_than = Type(self._client, 'type-less-than-href')
        self.assertTrue(type_less_than < self.__type)
        self.assertFalse(type_less_than > self.__type)

    def test_security(self):
        self.assertIsInstance(self.__type.security, Security)