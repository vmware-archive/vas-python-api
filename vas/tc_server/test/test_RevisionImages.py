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


from vas.tc_server.RevisionImages import RevisionImages, RevisionImage
from vas.tc_server.Revisions import Revision
from vas.test.VasTestCase import VasTestCase

class TestRevisionImages(VasTestCase):
    def test_list(self):
        self._assert_collection(RevisionImages(self._client, 'https://localhost:8443/tc-server/v1/revision-images/'))

    def test_create(self):
        location = 'https://localhost:8443/tc-server/v1/revision-images/'
        self._return_location('https://localhost:8443/tc-server/v1/revision-images/0/')

        revision_image = RevisionImages(self._client, location).create('/tmp/petcare-1.0.0.RELEASE.war', 'example',
            '1.0.0')

        self.assertIsInstance(revision_image, RevisionImage)
        self._assert_post_multipart(location, '/tmp/petcare-1.0.0.RELEASE.war', {'name': 'example', 'version': '1.0.0'})

    def test_detail(self):
        self._assert_item(RevisionImage(self._client, 'https://localhost:8443/tc-server/v1/revision-images/0/'), [
            ('name', 'example'),
            ('size', 5673284),
            ('version', '1.0.0'),
            ('revisions', [
                Revision(self._client,
                    'https://localhost:8443/tc-server/v1/groups/5/instances/6/applications/7/revisions/8/'),
                Revision(self._client,
                    'https://localhost:8443/tc-server/v1/groups/1/instances/2/applications/3/revisions/4/')
            ])
        ])

    def test_delete(self):
        self._assert_deletable(RevisionImage(self._client, 'https://localhost:8443/tc-server/v1/revision-images/0/'))
