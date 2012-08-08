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


from vas.shared.NamedImage import NamedImage
from vas.util.LinkUtils import LinkUtils

class RabbitMqPluginImage(NamedImage):
    """A plugin image

    :ivar str name: The name of the plugin image
    :ivar `vas.shared.Security` security:   The security configuration for the plugin image
    :ivar list plugins: The :class:`vas.rabbitmq.RabbitMqGroupPlugin` s that use the plugin image
    :ivar int size: The size of the plugin image
    :ivar str version: The version of the plugin image
    """

    __REL_PLUGIN = 'plugin'

    @property
    def plugins(self):
        return [RabbitMqGroupPlugin(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_PLUGIN)]


from vas.rabbitmq.RabbitMqGroupPlugin import RabbitMqGroupPlugin
