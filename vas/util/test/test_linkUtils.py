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


from vas.test.test_TestRoot import TestRoot
from vas.util.LinkUtils import LinkUtils
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class TestLinkUtils(TestRoot):
    _PAYLOADS = dict()

    _PAYLOADS['collection-href'] = {
        'links': [{
            'rel': 'self',
            'href': 'self-1'
        }],
        'collection-key': [{
            'links': [{
                'rel': 'foo',
                'href': 'foo-1'
            }, {
                'rel': 'self',
                'href': 'self-2'
            }]
        }, {
            'links': [{
                'rel': 'foo',
                'href': 'foo-2'
            }, {
                'rel': 'bar',
                'href': 'bar-1'
            }, {
                'rel': 'self',
                'href': 'self-3'
            }]
        }]
    }

    _PAYLOADS['item-href'] = {
        'key': 'value',
        'links': [{
            'rel': 'foo',
            'href': 'foo-href'
        }, {
            'rel': 'bar',
            'href': 'bar-href-1'
        }, {
            'rel': 'bar',
            'href': 'bar-href-1'
        }, {
            'rel': 'bar',
            'href': 'bar-href-2'
        }]
    }

    def setUp(self):
        super(TestLinkUtils, self).setUp()

    def test_get_collection_self_links(self):
        links = LinkUtils.get_collection_self_links(self._PAYLOADS['collection-href'], 'collection-key')
        self.assertEqual(['self-2', 'self-3'], links)

    def test_get_link_single(self):
        link = LinkUtils.get_link(self._PAYLOADS['item-href'], 'foo')
        self.assertEqual('foo-href', link)

    def test_get_link_multiple(self):
        self.assertRaises(VFabricAdministrationServerError, LinkUtils.get_link, self._PAYLOADS['item-href'], 'bar')

    def test_get_links_no_rel(self):
        links = LinkUtils.get_links(self._PAYLOADS['item-href'])
        self.assertEqual({'foo': ['foo-href'], 'bar': ['bar-href-1', 'bar-href-2']}, links)

    def test_get_links_with_rel(self):
        links = LinkUtils.get_links(self._PAYLOADS['item-href'], 'bar')
        self.assertEqual(['bar-href-1', 'bar-href-2'], links)
