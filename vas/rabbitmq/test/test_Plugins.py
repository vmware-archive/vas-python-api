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


from vas.rabbitmq.Instances import Instance
from vas.rabbitmq.PluginImages import PluginImage
from vas.rabbitmq.Plugins import Plugins, Plugin
from vas.test.VasTestCase import VasTestCase


class TestPlugins(VasTestCase):
    def test_list(self):
        self._assert_collection(
            Plugins(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/'), 3)

    def test_create(self):
        plugin_image_location = 'https://localhost:8443/rabbitmq/v1/plugin-images/0/'
        location = 'https://localhost:8443/rabbitmq/v1/groups/2/instances/3/plugins/6/'
        self._return_location('https://localhost:8443/rabbitmq/v1/groups/2/instances/3/plugins/6/')

        plugin = Plugins(self._client, location).create(PluginImage(self._client, plugin_image_location))

        self.assertIsInstance(plugin, Plugin)
        self._assert_post(location, {'image': plugin_image_location}, 'plugin')

    def test_detail(self):
        self._assert_item(Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/'), [
            ('name', 'example'),
            ('version', '1.0.0'),
            ('instance', lambda actual: self.assertIsInstance(actual, Instance)),
            ('plugin_image', lambda actual: self.assertIsInstance(actual, PluginImage)),
            ('state', 'ENABLED')
        ])

    def test_delete(self):
        self._assert_deletable(
            Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/'))

    def test_enable(self):
        Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/').enable()
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/state/',
            {'status': 'ENABLED'})

    def test_disable(self):
        Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/').disable()
        self._assert_post('https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/state/',
            {'status': 'DISABLED'})
