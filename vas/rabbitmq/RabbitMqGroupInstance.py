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


from vas.shared.GroupInstance import GroupInstance

class RabbitMqGroupInstance(GroupInstance):
    """A RabbitMQ group instance


    :ivar `vas.rabbitmq.RabbitMqGroup` group: The group instance's parent group
    :ivar `vas.rabbitmq.RabbitMqInstallation` installation: The group instance's installation
    :ivar `vas.rabbitmq.RabbitMqLiveConfigurations` live_configurations:  The collection of live configurations
    :ivar str name: The name of the group instance
    :ivar list node_instances: The :class:`vas.rabbitmq.RabbitMqNodeInstance` s that are members of the group instance
    :ivar `vas.rabbitmq.RabbitMqPendingConfigurations` pending_configurations: The collection of pending configurations
    :ivar `vas.rabbitmq.RabbitMqGroupPlugins` plugins:   The collection of plugins
    :ivar `vas.shared.Security` security:   The security configuration for group instance
    :ivar str state:    The current state of the group instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __REL_NODE_INSTANCE = 'node-instance'

    __REL_PLUGINS = 'plugins'

    def __init__(self, client, location):
        super(RabbitMqGroupInstance, self).__init__(client, location, self.__REL_NODE_INSTANCE)

        self.plugins = RabbitMqGroupPlugins(client, self._links[self.__REL_PLUGINS][0])


    def update(self, installation):
        """Update the group instance to use a different installation

        :type installation:    :class:`vas.rabbitmq.RabbitMqInstallation`
        :param installation:   The installation to use when running the instance
        """

        self._client.post(self._location_self, {'installation': installation._location_self})

    def _create_group(self, client, location):
        return RabbitMqGroup(client, location)

    def _create_installation(self, client, location):
        return RabbitMqInstallation(client, location)

    def _create_live_configurations(self, client, location):
        return RabbitMqLiveConfigurations(client, location)

    def _create_node_instance(self, client, location):
        return RabbitMqNodeInstance(client, location)

    def _create_pending_configurations(self, client, location):
        return RabbitMqPendingConfigurations(client, location)

from vas.rabbitmq.RabbitMqGroup import RabbitMqGroup
from vas.rabbitmq.RabbitMqInstallation import RabbitMqInstallation
from vas.rabbitmq.RabbitMqLiveConfigurations import RabbitMqLiveConfigurations
from vas.rabbitmq.RabbitMqNodeInstance import RabbitMqNodeInstance
from vas.rabbitmq.RabbitMqPendingConfigurations import RabbitMqPendingConfigurations
from vas.rabbitmq.RabbitMqGroupPlugins import RabbitMqGroupPlugins
