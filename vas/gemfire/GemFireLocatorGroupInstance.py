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

class GemFireLocatorGroupInstance(GroupInstance):
    """A GemFire locator group instance


    :ivar str address: The name of the property, configured in the ``agent.properties`` file, that will be used to
                       configure the address of the network card on which the locator will listen
    :ivar `vas.gemfire.GemFireGroup` group: The group instance's parent group
    :ivar `vas.gemfire.GemFireInstallation` installation: The group instance's installation
    :ivar `vas.gemfire.GemFireLocatorLiveConfigurations` live_configurations:  The collection of live configurations
    :ivar str name: The name of the group instance
    :ivar list node_instances: The :class:`vas.gemfire.GemFireLocatorNodeInstance` s that are members of the group instance
    :ivar bool peer:  Whether the locator is acting as a peer
    :ivar `vas.gemfire.GemFireLocatorPendingConfigurations` pending_configurations: The collection of pending configurations
    :ivar int port: The port on which the locator is listening on
    :ivar `vas.shared.Security` security:   The security configuration for group instance
    :ivar bool server: Whether the locator is acting as a server
    :ivar str state:    The current state of the group instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __KEY_ADDRESS = 'address'

    __KEY_PEER = 'peer'

    __KEY_PORT = 'port'

    __KEY_SERVER = 'server'

    __REL_NODE_INSTANCE = 'locator-node-instance'

    def __init__(self, client, location):
        super(GemFireLocatorGroupInstance, self).__init__(client, location, self.__REL_NODE_INSTANCE)

        self.address = self._details[self.__KEY_ADDRESS]
        self.peer = self._details[self.__KEY_PEER]
        self.port = self._details[self.__KEY_PORT]
        self.server = self._details[self.__KEY_SERVER]

    def update(self, installation=None, address=None, peer=None, port=None, server=None):
        """Update the locator group instance to use a different installation

        :type installation:    :class:`vas.gemfire.GemFireInstallation`
        :param installation:   The installation to use when running the instance
        :type address:     :obj:`str`
        :param address:    The name of the property, configured in the ``agent.properties`` file, that will be used to
                           configure the address of the network card on which the locator will listen
        :type peer:     :obj:`bool`
        :param peer:    Whether the locator should act as a peer
        :type port:     :obj:`int`
        :param port:    The port on which the locator should listen on
        :type server:     :obj:`bool`
        :param server:    Whether the locator should act as a server
        """

        payload = dict()

        if installation is not None:
            payload['installation'] = installation._location_self

        if address is not None:
            payload['address'] = address

        if peer is not None:
            payload['peer'] = peer

        if port is not None:
            payload['port'] = port

        if server is not None:
            payload['server'] = server

        self._client.post(self._location_self, payload)

    def _create_group(self, client, location):
        return GemFireGroup(client, location)

    def _create_installation(self, client, location):
        return GemFireInstallation(client, location)

    def _create_live_configurations(self, client, location):
        return GemFireLocatorLiveConfigurations(client, location)

    def _create_node_instance(self, client, location):
        return GemFireLocatorNodeInstance(client, location)

    def _create_pending_configurations(self, client, location):
        return GemFireLocatorPendingConfigurations(client, location)

from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireInstallation import GemFireInstallation
from vas.gemfire.GemFireLocatorLiveConfigurations import GemFireLocatorLiveConfigurations
from vas.gemfire.GemFireLocatorNodeInstance import GemFireLocatorNodeInstance
from vas.gemfire.GemFireLocatorPendingConfigurations import GemFireLocatorPendingConfigurations
