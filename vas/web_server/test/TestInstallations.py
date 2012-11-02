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


from vas.web_server.Groups import Group
from vas.web_server.InstallationImages import InstallationImage
from vas.web_server.Installations import Installations, Installation
from vas.web_server.Instances import Instance
from vas.test.VasTestCase import VasTestCase

class TestInstallations(VasTestCase):
    def test_list(self):
        self._assert_collection(
            Installations(self._client, 'https://localhost:8443/web-server/v1/groups/1/installations/'))

    def test_create(self):
        installation_image_location = 'https://localhost:8443/web-server/v1/installation-images/0/'
        location = 'https://localhost:8443/web-server/v1/groups/1/installations/'
        self._return_location('https://localhost:8443/web-server/v1/groups/1/installations/2/')

        installation = Installations(self._client, location).create(
            InstallationImage(self._client, installation_image_location))

        self.assertIsInstance(installation, Installation)
        self._assert_post(location, {'image': installation_image_location}, 'installation')

    def test_detail(self):
        self._assert_item(Installation(self._client, 'https://localhost:8443/web-server/v1/groups/1/installations/2/'),
            [
                ('version', '2.8.1'),
                ('group', lambda actual: self.assertIsInstance(actual, Group)),
                ('instances', [Instance(self._client, 'https://localhost:8443/web-server/v1/groups/1/instances/4/'),
                               Instance(self._client, 'https://localhost:8443/web-server/v1/groups/1/instances/3/')]),
                ('installation_image', lambda actual: self.assertIsInstance(actual, InstallationImage))
            ])

    def test_delete(self):
        self._assert_deletable(
            Installation(self._client, 'https://localhost:8443/web-server/v1/groups/1/installations/2/'))
