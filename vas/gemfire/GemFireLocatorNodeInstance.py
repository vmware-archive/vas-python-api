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


from vas.shared.NodeInstance import NodeInstance

class GemFireLocatorNodeInstance(NodeInstance):
    """A GemFire locator node instance

    :ivar str address: The name of the property, configured in the ``agent.properties`` file, that will be used to
                       configure the address of the network card on which the locator will listen
    :ivar `vas.gemfire.GemFireLocatorGroupInstance` group_instance: The group instance that the node instance is a member of
    :ivar `vas.gemfire.GemFireLocatorLogs` logs: The collection of logs
    :ivar str name: The name of the node instance
    :ivar `vas.gemfire.GemFireNode` node: The node instance's parent node
    :ivar bool peer:  Whether the locator is acting as a peer
    :ivar int port: The port on which the locator is listening on
    :ivar `vas.shared.Security` security: The security configuration for the node instance
    :ivar bool server: Whether the locator is acting as a server
    :ivar str state:    The current state of the node instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __KEY_ADDRESS = 'address'

    __KEY_PEER = 'peer'

    __KEY_PORT = 'port'

    __KEY_SERVER = 'server'

    __REL_GROUP_INSTANCE = 'locator-group-instance'

    def __init__(self, client, location):
        super(GemFireLocatorNodeInstance, self).__init__(client, location, self.__REL_GROUP_INSTANCE)

        self.address = self._details[self.__KEY_ADDRESS]
        self.peer = self._details[self.__KEY_PEER]
        self.port = self._details[self.__KEY_PORT]
        self.server = self._details[self.__KEY_SERVER]

    def start(self):
        """Start the instance by attempting to set its ``status`` to ``STARTED``"""

        self._client.post(self._location_state, {'status': 'STARTED'})

    def _create_group_instance(self, client, location):
        return GemFireLocatorGroupInstance(client, location)

    def _create_logs(self, client, location):
        return GemFireLocatorLogs(client, location)

    def _create_node(self, client, location):
        return GemFireNode(client, location)

from vas.gemfire.GemFireLocatorGroupInstance import GemFireLocatorGroupInstance
from vas.gemfire.GemFireLocatorLogs import GemFireLocatorLogs
from vas.gemfire.GemFireNode import GemFireNode
