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


from vas.shared.MutableCollection import MutableCollection
import vas.shared.Instance
from vas.util.LinkUtils import LinkUtils

class Instances(MutableCollection):
    """Used to enumerate, create, and delete RabbitMQ instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Instances, self).__init__(client, location, 'group-instances', Instance)


    def create(self, installation, name):
        """Creates a new instance

        :param str                                          name:           The name of the group instance
        :param `vas.rabbitmq.Installations.Installation`    installation:   The installation to be used by the instance
        :rtype:         :class:`vas.rabbitmq.Instances.Instance`
        :return:        The new instance
        """

        payload = {'name': name, 'installation': installation._location}
        return self._create(payload, 'group-instance')


class Instance(vas.shared.Instance.Instance):
    """A RabbitMQ instance

    :ivar `vas.rabbitmq.Groups.Group`               group:          The group that contains this instance
    :ivar `vas.rabbitmq.Installations.Installation` installation:   The installation that this instance is using
    :ivar `vas.rabbitmq.LiveConfiguration.LiveConfiguration`    live_configurations:    The instance's live
                                                                                        configurations
    :ivar str                                       name:           The instance's name
    :ivar list                                      node_instances: The instance's individual node instances
    :ivar `vas.rabbitmq.PendingConfigurations.PendingConfiguration` pending_configurations: The instance's pending
                                                                                            configurations
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar str                                       state:          Retrieves the state of the resource from the server.
                                                                    Will be one of:

                                                                    * ``STARTING``
                                                                    * ``STARTED``
                                                                    * ``STOPPING``
                                                                    * ``STOPPED``
    """

    __plugins = None

    @property
    def plugins(self):
        self.__plugins = self.__plugins or Plugins(self._client, self.__plugins_location)
        return self.__plugins

    def __init__(self, client, location):
        super(Instance, self).__init__(client, location, Group, Installation, LiveConfigurations, PendingConfigurations,
            NodeInstance, 'node-instance')
        self.__plugins_location = LinkUtils.get_link_href(self._details, 'plugins')

    def update(self, installation):
        """Updates the instance to use a different installation

        :param `vas.rabbitmq.Installations.Installation`    installation:   The installation that the instance should use
        """

        self._client.post(self._location, {'installation': installation._location})
        self.reload()


from vas.rabbitmq.Groups import Group
from vas.rabbitmq.Installations import Installation
from vas.rabbitmq.LiveConfigurations import LiveConfigurations
from vas.rabbitmq.NodeInstances import NodeInstance
from vas.rabbitmq.PendingConfigurations import PendingConfigurations
from vas.rabbitmq.Plugins import Plugins
