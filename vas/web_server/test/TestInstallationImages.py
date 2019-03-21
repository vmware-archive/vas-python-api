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


from vas.web_server.InstallationImages import InstallationImages, InstallationImage
from vas.web_server.Installations import Installation
from vas.test.VasTestCase import VasTestCase

class TestInstallationImages(VasTestCase):
    def test_list(self):
        self._assert_collection(
            InstallationImages(self._client, 'https://localhost:8443/web-server/v1/installation-images/'))

    def test_create(self):
        location = 'https://localhost:8443/web-server/v1/installation-images/'
        self._return_location('https://localhost:8443/web-server/v1/installation-images/0/')

        installation_image = InstallationImages(self._client,
            'https://localhost:8443/web-server/v1/installation-images/').create(
            '/tmp/vfabric-web-server-standard-2.8.0.RELEASE.zip', '2.8.0.RELEASE', 'x64', 'Linux')

        self.assertIsInstance(installation_image, InstallationImage)
        self._assert_post_multipart(location, '/tmp/vfabric-web-server-standard-2.8.0.RELEASE.zip',
            {'version': '2.8.0.RELEASE', 'architecture': 'x64', 'operating-system': 'Linux'})

    def test_detail(self):
        self._assert_item(
            InstallationImage(self._client, 'https://localhost:8443/web-server/v1/installation-images/0/'), [
                ('architecture', 'x64'),
                ('operating_system', 'Linux'),
                ('size', 7340032),
                ('version', '2.8.1'),
                ('installations',
                 [Installation(self._client, 'https://localhost:8443/web-server/v1/groups/1/installations/2/'),
                  Installation(self._client, 'https://localhost:8443/web-server/v1/groups/3/installations/4/')])
            ])

    def test_delete(self):
        self._assert_deletable(
            InstallationImage(self._client, 'https://localhost:8443/web-server/v1/installation-images/0/'))
