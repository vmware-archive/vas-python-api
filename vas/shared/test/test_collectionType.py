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


from mock import MagicMock
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.CollectionType import CollectionType
from vas.shared.Type import Type
from vas.test.test_TestRoot import TestRoot

class TestCollectionType(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['collection-type-href'] = {
        'collection-key': [{
            'links': [{
                'rel': 'self',
                'href': 'self-href'
            }, {
                'rel': 'security',
                'href': 'security-href'
            }]
        }],
        'links': [{
            'rel': 'self',
            'href': 'collection-type-href'
        }, {
            'rel': 'security',
            'href': 'security-href'
        }]
    }

    _PAYLOADS['single-type-href'] = {
        'links': [{
            'rel': 'security',
            'href': 'security-href'
        }, {
            'rel': 'self',
            'href': 'single-type-self-href'
        }]
    }


    def setUp(self):
        super(TestCollectionType, self).setUp()
        self.__collection_type = CollectionType(self._client, 'collection-type-href', 'collection-key')
        self.__single_type = Type(self._client, 'single-type-href')

        create_item = MagicMock()
        create_item.return_value = self.__single_type
        self.__collection_type._create_item = create_item

    def test_delete(self):
        self.__collection_type.delete(self.__single_type)

        self._client.delete.assert_called_with('single-type-self-href')

    def test__create_item(self):
        self.assertRaises(VFabricAdministrationServerError,
                          CollectionType(self._client, 'collection-type-href', 'collection-key')._create_item, 'href')

    def test_iterator(self):
        count = 0
        #noinspection PyUnusedLocal
        for item in self.__collection_type:
            count += 1

        self.assertEqual(1, count)
