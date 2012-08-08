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
from vas.test.StubClient import StubClient
from vas.util.LinkUtils import LinkUtils
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class TestLinkUtils(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()

    def test_get_collection_self_links(self):
        links = LinkUtils.get_collection_self_links(self.__client.get('https://localhost:8443/vfabric/v1/nodes/'),
            'nodes')
        self.assertEqual(['https://localhost:8443/vfabric/v1/nodes/0/', 'https://localhost:8443/vfabric/v1/nodes/1/'],
            links)

    def test_get_link_single(self):
        link = LinkUtils.get_link(self.__client.get('https://localhost:8443/vfabric/v1/'), 'nodes')
        self.assertEqual('https://localhost:8443/vfabric/v1/nodes/', link)

    def test_get_link_multiple(self):
        self.assertRaises(VFabricAdministrationServerError, LinkUtils.get_link,
            self.__client.get('https://localhost:8443/tc-server/v1/groups/0/'), 'node')

    def test_get_links_no_rel(self):
        links = LinkUtils.get_links(self.__client.get('https://localhost:8443/vfabric/v1/'))
        self.assertEqual({'agent-image': ['https://localhost:8443/vfabric/v1/agent-image/'],
                          'nodes': ['https://localhost:8443/vfabric/v1/nodes/'],
                          'tasks': ['https://localhost:8443/vfabric/v1/tasks/']}, links)

    def test_get_links_with_rel(self):
        links = LinkUtils.get_links(self.__client.get('https://localhost:8443/tc-server/v1/groups/0/'), 'node')
        self.assertEqual(
            ['https://localhost:8443/tc-server/v1/nodes/1/', 'https://localhost:8443/tc-server/v1/nodes/0/'], links)

    def test_repr(self):
        linkUtils = LinkUtils()
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(linkUtils)), '__repr__ method has not been specified')
        eval(repr(linkUtils))
