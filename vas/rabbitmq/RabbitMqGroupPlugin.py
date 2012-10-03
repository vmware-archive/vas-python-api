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


from vas.shared.Type import Type

class RabbitMqGroupPlugin(Type):
    """A RabbitMQ group plugin

    :ivar `vas.rabbitmq.RabbitMqGroupInstance` instance: The group plugin's parent group instance
    :ivar str name: The name of the group plugin
    :ivar `vas.rabbitmq.RabbitMqPluginImage` plugin_image: The image the plugin is based on
    :ivar `vas.shared.Security` security:   The security configuration for the group plugin
    :ivar str version: The version of the group plugin
    :ivar str state:    The current state of the group plugin.  Will be one of the following:

                        * ``ENABLING``
                        * ``ENABLED``
                        * ``IMPLICITLY_ENABLED``
                        * ``DISABLING``
                        * ``DISABLED``
    """

    __KEY_NAME = 'name'

    __KEY_VERSION = 'version'

    __REL_GROUP_INSTANCE = 'group-instance'

    __REL_PLUGIN_IMAGE = 'plugin-image'

    __REL_STATE = 'state'

    def __init__(self, client, location):
        super(RabbitMqGroupPlugin, self).__init__(client, location)

        self.__location_state = self._links[self.__REL_STATE][0]

        self.name = self._details[self.__KEY_NAME]
        self.version = self._details[self.__KEY_VERSION]
        self.instance = RabbitMqGroupInstance(client, self._links[self.__REL_GROUP_INSTANCE][0])

        if self.__REL_PLUGIN_IMAGE in self._links:
            self.plugin_image = RabbitMqPluginImage(client, self._links[self.__REL_PLUGIN_IMAGE][0])
        else:
            self.plugin_image = None

    @property
    def state(self):
        return self._client.get(self.__location_state)['status']

    def enable(self):
        """Start the plugin by attempting to set its ``status`` to ``ENABLED``"""

        self._client.post(self.__location_state, {'status': 'ENABLED'})

    def disable(self):
        """Stop the plugin by attempting to set its ``status`` to ``DISABLED``"""

        self._client.post(self.__location_state, {'status': 'DISABLED'})

from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
from vas.rabbitmq.RabbitMqPluginImage import RabbitMqPluginImage
