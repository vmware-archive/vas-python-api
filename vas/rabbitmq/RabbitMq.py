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


from vas.shared.ComponentType import ComponentType

class RabbitMq(ComponentType):
    """The RabbitMQ component of the vFabric Administration Server

    :ivar `vas.rabbitmq.RabbitMqGroups` groups:    The collection of groups
    :ivar `vas.rabbitmq.RabbitMqInstallationImages` installation_images:  The collection of installation images
    :ivar `vas.rabbitmq.RabbitMqNodes` nodes: The collection of nodes
    :ivar `vas.rabbitmq.RabbitMqPluginImages` plugin_images: The collection of plugin images
    """

    __REL_PLUGIN_IMAGES = 'plugin-images'

    __ROOT_PATH = '/rabbitmq/v1/'

    def __init__(self, client, location_stem):
        super(RabbitMq, self).__init__(client, location_stem.format(self.__ROOT_PATH))

        self.plugin_images = RabbitMqPluginImages(client, self._links[self.__REL_PLUGIN_IMAGES][0])
        self.__location_stem = location_stem

    def _create_groups(self, client, location):
        return RabbitMqGroups(client, location)

    def _create_installation_images(self, client, location):
        return RabbitMqInstallationImages(client, location)

    def _create_nodes(self, client, location):
        return RabbitMqNodes(client, location)

    def __repr__(self):
        return "{}(client={}, location_stem={})".format(self.__class__.__name__, self._client,
            repr(self.__location_stem))

from vas.rabbitmq.RabbitMqInstallationImages import RabbitMqInstallationImages
from vas.rabbitmq.RabbitMqPluginImages import RabbitMqPluginImages
from vas.rabbitmq.RabbitMqGroups import RabbitMqGroups
from vas.rabbitmq.RabbitMqNodes import RabbitMqNodes
