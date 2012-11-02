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


from vas.rabbitmq.PluginImages import PluginImages, PluginImage
from vas.rabbitmq.Plugins import Plugin
from vas.test.VasTestCase import VasTestCase

class TestPluginImages(VasTestCase):
    def test_list(self):
        self._assert_collection(PluginImages(self._client, 'https://localhost:8443/rabbitmq/v1/plugin-images/'))

    def test_create(self):
        location = 'https://localhost:8443/rabbitmq/v1/plugin-images/'
        self._return_location('https://localhost:8443/rabbitmq/v1/plugin-images/0/')

        plugin_image = PluginImages(self._client, location).create('/tmp/plugin-image.zip')

        self.assertIsInstance(plugin_image, PluginImage)
        self._assert_post_multipart('https://localhost:8443/rabbitmq/v1/plugin-images/', '/tmp/plugin-image.zip')

    def test_detail(self):
        self._assert_item(PluginImage(self._client, 'https://localhost:8443/rabbitmq/v1/plugin-images/0/'), [
            ('name', 'example'),
            ('size', 5673284),
            ('version', '1.0.0'),
            ('plugins', [Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/4/instances/5/plugins/6/'),
                         Plugin(self._client, 'https://localhost:8443/rabbitmq/v1/groups/1/instances/2/plugins/3/')])
        ])

    def test_delete(self):
        self._assert_deletable(PluginImage(self._client, 'https://localhost:8443/rabbitmq/v1/plugin-images/0/'))
