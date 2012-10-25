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


from vas.tc_server.Applications import Application
from vas.tc_server.NodeApplications import NodeApplications, NodeApplication
from vas.tc_server.NodeInstances import NodeInstance
from vas.tc_server.NodeRevisions import NodeRevisions
from vas.test.VasTestCase import VasTestCase

class TestNodeApplications(VasTestCase):
    def test_list(self):
        self._assert_collection(
            NodeApplications(self._client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/'))

    def test_detail(self):
        self._assert_item(
            NodeApplication(self._client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/'), [
                ('context_path', '/example'),
                ('host', 'localhost'),
                ('name', 'Example'),
                ('service', 'Catalina'),
                ('group_application', lambda actual: self.assertIsInstance(actual, Application)),
                ('instance', lambda actual: self.assertIsInstance(actual, NodeInstance)),
                ('revisions', lambda actual: self.assertIsInstance(actual, NodeRevisions))
            ])
