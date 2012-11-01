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


from vas.gemfire.AgentInstances import AgentInstance
from vas.gemfire.CacheServerInstances import CacheServerInstance
from vas.gemfire.Groups import Group
from vas.gemfire.InstallationImages import InstallationImage
from vas.gemfire.Installations import Installations, Installation
from vas.gemfire.LocatorInstances import LocatorInstance
from vas.test.VasTestCase import VasTestCase

class TestInstallations(VasTestCase):
    def test_list(self):
        self._assert_collection(
            Installations(self._client, 'https://localhost:8443/gemfire/v1/groups/1/installations/'))


    def test_create(self):
        installation_image_location = 'https://localhost:8443/gemfire/v1/installation-images/0/'
        location = 'https://localhost:8443/gemfire/v1/groups/0/installations/'
        self._return_location('https://localhost:8443/gemfire/v1/groups/1/installations/2/')

        installation = Installations(self._client, location).create(
            InstallationImage(self._client, installation_image_location))

        self.assertIsInstance(installation, Installation)
        self._assert_post(location, {'image': installation_image_location}, 'installation')

    def test_detail(self):
        self._assert_item(Installation(self._client, 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'), [
            ('version', '6.6.1'),
            ('group', lambda actual: self.assertIsInstance(actual, Group)),
            ('agent_instances', [
                AgentInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/1/agent-instances/3/')
            ]),
            ('cache_server_instances', [
                CacheServerInstance(self._client,
                    'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/5/'),
                CacheServerInstance(self._client,
                    'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/6/')
            ]),
            ('installation_image', lambda actual: self.assertIsInstance(actual, InstallationImage)),
            ('locator_instances', [
                LocatorInstance(self._client, 'https://localhost:8443/gemfire/v1/groups/1/locator-instances/4/')
            ])
        ])

    def test_delete(self):
        self._assert_deletable(
            Installation(self._client, 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'))
