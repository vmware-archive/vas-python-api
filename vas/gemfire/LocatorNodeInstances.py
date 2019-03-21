# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.shared.NodeInstances import NodeInstances, NodeInstance

class LocatorNodeInstances(NodeInstances):
    """Used to enumerate locator instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorNodeInstances, self).__init__(client, location, 'locator-node-instances', LocatorNodeInstance)


class LocatorNodeInstance(NodeInstance):
    """A locator node instance

    :ivar str                                               address:        The address of the network card on which the
                                                                            locator will listen
    :ivar `vas.gemfire.LocatorInstances.LocatorInstance`    group_instance: The node instance's group instance
    :ivar `vas.gemfire.LocatorLiveConfigurations.LocatorLiveConfigurations` live_configurations:    The node instance's
                                                                                                    live configuration
    :ivar `vas.gemfire.LocatorLogs.LocatorLogs`             logs:           The instance's logs
    :ivar str                                               name:           The instance's name
    :ivar `vas.gemfire.Nodes.Nodes`                         node:           The node that contains this instance
    :ivar bool                                              peer:           `True`` if the locator will act as a peer,
                                                                            `False` if it will not
    :ivar int                                               port:           The port that the locator will listen on
    :ivar `vas.shared.Security.Security`                    security:       The resource's security
    :ivar bool                                              server:         `True` if the locator will act as a server,
                                                                            `False` if it will not
    :ivar str                                               state:          Retrieves the state of the resource from the
                                                                            server. Will be one of:

                                                                            * ``STARTING``
                                                                            * ``STARTED``
                                                                            * ``STOPPING``
                                                                            * ``STOPPED``
    """

    @property
    def address(self):
        return self.__address

    @property
    def peer(self):
        return self.__peer

    @property
    def port(self):
        return self.__port

    @property
    def server(self):
        return self.__server

    def __init__(self, client, location):
        super(LocatorNodeInstance, self).__init__(client, location, Node, LocatorLogs, LocatorInstance,
            'locator-group-instance', LocatorNodeLiveConfigurations)

    def reload(self):
        """Reloads the instance's details from the server"""

        super(LocatorNodeInstance, self).reload()

        self.__address = self._details['address']
        self.__peer = self._details['peer']
        self.__port = self._details['port']
        self.__server = self._details['server']

    def __str__(self):
        return "<{} name={} port={} peer={} server={} address={}>".format(self.__class__.__name__, self.name,
            self.__port, self.__peer, self.__server, self.__address)


from vas.gemfire.LocatorInstances import LocatorInstance
from vas.gemfire.LocatorLogs import LocatorLogs
from vas.gemfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfigurations
from vas.gemfire.Nodes import Node
