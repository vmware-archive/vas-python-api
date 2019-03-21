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


from vas.tc_server.NodeApplications import NodeApplication
from vas.tc_server.NodeRevisions import NodeRevisions, NodeRevision
from vas.tc_server.Revisions import Revision
from vas.test.VasTestCase import VasTestCase

class TestNodeRevisions(VasTestCase):
    def test_list(self):
        self._assert_collection(NodeRevisions(self._client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/'))

    def test_detail(self):
        self._assert_item(NodeRevision(self._client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/'), [
            ('state', 'STOPPED'),
            ('version', '1.0.0'),
            ('group_revision', lambda actual: self.assertIsInstance(actual, Revision)),
            ('application', lambda actual: self.assertIsInstance(actual, NodeApplication))
        ])

    def test_start(self):
        NodeRevision(self._client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/').start()
        self._assert_post('https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/state/',
            {'status': 'STARTED'})

    def test_stop(self):
        NodeRevision(self._client,
            'https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/').stop()
        self._assert_post('https://localhost:8443/tc-server/v1/nodes/0/instances/3/applications/5/revisions/7/state/',
            {'status': 'STOPPED'})
