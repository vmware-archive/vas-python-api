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


from vas.rabbitmq.Groups import Groups
from vas.rabbitmq.InstallationImages import InstallationImages
from vas.rabbitmq.Nodes import Nodes
from vas.rabbitmq.PluginImages import PluginImages
from vas.rabbitmq.RabbitMq import RabbitMq
from vas.test.VasTestCase import VasTestCase

class TestRabbitMq(VasTestCase):
    def test_rabbitmq(self):
        self._assert_item(RabbitMq(self._client, 'https://localhost:8443/rabbitmq/v1/'), [
            ('groups', lambda actual: self.assertIsInstance(actual, Groups)),
            ('installation_images', lambda actual: self.assertIsInstance(actual, InstallationImages)),
            ('nodes', lambda actual: self.assertIsInstance(actual, Nodes)),
            ('plugin_images', lambda actual: self.assertIsInstance(actual, PluginImages))
        ], False)
