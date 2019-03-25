# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.tc_server.Instances import Instance
from vas.tc_server.PendingConfigurations import PendingConfigurations, PendingConfiguration
from vas.test.VasTestCase import VasTestCase

class TestPendingConfigurations(VasTestCase):
    def test_list(self):
        self._assert_collection(PendingConfigurations(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/'), 3)

    def test_create(self):
        content = 'configuration-content'
        location = 'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/2/')

        configuration = PendingConfigurations(self._client, location).create('conf/server.xml', content)

        self.assertIsInstance(configuration, PendingConfiguration)
        self._assert_post_multipart(location, 'configuration-content', {'path': 'conf/server.xml'})

    def test_detail(self):
        self._assert_item(PendingConfiguration(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/2/'), [
            ('path', 'conf/server.xml'),
            ('size', 10537),
            ('content', 'groups-instances-configurations-pending-content\n'),
            ('instance', lambda actual: self.assertIsInstance(actual, Instance))
        ])

    def test_delete(self):
        self._assert_deletable(PendingConfiguration(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/2/'))

    def test_set_content(self):
        #noinspection PyPropertyAccess
        PendingConfiguration(self._client,
            'https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/2/').content = 'new-content'

        self._assert_post('https://localhost:8443/tc-server/v1/groups/0/instances/1/configurations/pending/2/content/',
            'new-content')
