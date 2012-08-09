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


from vas.shared.MutableCollectionType import MutableCollectionType

class RabbitMqGroupPlugins(MutableCollectionType):
    """A collection of RabbitMQ group plugins

    :ivar `vas.shared.Security` security:   The security configuration for the collection of group plugins
    """

    __COLLECTION_KEY = 'plugins'

    __REL_PLUGIN = 'plugin'

    def __init__(self, client, location):
        super(RabbitMqGroupPlugins, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, plugin_image):
        """Create a new plugin

        :type plugin_image:   :class:`vas.rabbitmq.RabbitMqPluginImage`
        :param plugin_image:  The plugin image to use when creating this plugin
        :rtype:         :class:`vas.rabbitmq.RabbitMqGroupPlugin`
        :return:        The newly created plugin
        """

        location = self._client.post(self._location_self, {'image': plugin_image._location_self}, self.__REL_PLUGIN)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return RabbitMqGroupPlugin(client, location)

from vas.rabbitmq.RabbitMqGroupPlugin import RabbitMqGroupPlugin
