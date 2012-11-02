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


from vas.tc_server.Applications import Applications, Application
from vas.tc_server.Instances import Instance
from vas.tc_server.NodeApplications import NodeApplication
from vas.tc_server.Revisions import Revisions
from vas.test.VasTestCase import VasTestCase

class TestApplications(VasTestCase):
    def test_list(self):
        self._assert_collection(
            Applications(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/'))

    def test_create(self):
        location = 'https://localhost:8443/tc-server/v1/groups/0/instances/1/applications/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/')

        application = Applications(self._client, location).create('Example', '/Example', 'Catalina', 'localhost')

        self.assertIsInstance(application, Application)
        self._assert_post(location,
            {'context-path': '/Example', 'host': 'localhost', 'name': 'Example', 'service': 'Catalina'},
            'group-application')

    def test_detail(self):
        self._assert_item(
            Application(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/'), [
                ('context_path', '/example'),
                ('host', 'localhost'),
                ('name', 'Example'),
                ('service', 'Catalina'),
                ('instance', lambda actual: self.assertIsInstance(actual, Instance)),
                ('revisions', lambda actual: self.assertIsInstance(actual, Revisions)),
                ('node_applications', [
                    NodeApplication(self._client,
                        'https://localhost:8443/tc-server/v1/nodes/1/instances/5/applications/8/'),
                    NodeApplication(self._client,
                        'https://localhost:8443/tc-server/v1/nodes/0/instances/4/applications/7/')
                ])
            ])

    def test_delete(self):
        self._assert_deletable(
            Application(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/6/'))
