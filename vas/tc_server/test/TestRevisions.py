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


from vas.tc_server.Applications import Application
from vas.tc_server.NodeRevisions import NodeRevision
from vas.tc_server.RevisionImages import RevisionImage
from vas.tc_server.Revisions import Revisions, Revision
from vas.test.VasTestCase import VasTestCase

class TestRevisions(VasTestCase):
    def test_list(self):
        self._assert_collection(Revisions(self._client,
            'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/'))

    def test_create(self):
        revision_image_location = 'https://localhost:8443/tc-server/v1/revision-images/0/'
        location = 'https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/2/instances/3/applications/4/revisions/5/')

        revision = Revisions(self._client, location).create(RevisionImage(self._client, revision_image_location))

        self.assertIsInstance(revision, Revision)
        self._assert_post(location, {'image': revision_image_location}, 'group-revision')

    def test_detail(self):
        self._assert_item(Revision(self._client,
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/'), [
            ('version', '1.0.0'),
            ('state', 'STOPPED'),
            ('application', lambda actual: self.assertIsInstance(actual, Application)),
            ('revision_image', lambda actual: self.assertIsInstance(actual, RevisionImage)),
            ('node_revisions', [
                NodeRevision(self._client,
                    'https://localhost:8443/tc-server/v1/nodes/1/instances/6/applications/9/revisions/12/'),
                NodeRevision(self._client,
                    'https://localhost:8443/tc-server/v1/nodes/0/instances/5/applications/8/revisions/11/')
            ])
        ])

    def test_delete(self):
        self._assert_deletable(Revision(self._client,
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/'))

    def test_start(self):
        Revision(self._client,
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/').start()
        self._assert_post('https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/state/',
            {'status': 'STARTED'})

    def test_stop(self):
        Revision(self._client,
            'https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/').stop()
        self._assert_post('https://localhost:8443/tc-server/v1/groups/3/instances/4/applications/7/revisions/10/state/',
            {'status': 'STOPPED'})
