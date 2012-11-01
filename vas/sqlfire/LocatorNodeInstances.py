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


from vas.shared.NodeInstances import NodeInstances, NodeInstance

class LocatorNodeInstances(NodeInstances):
    """Used to enumerate locator instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorNodeInstances, self).__init__(client, location, 'locator-node-instances', LocatorNodeInstance)


class LocatorNodeInstance(NodeInstance):
    """A locator node instance

    :ivar str                                               bind_address:           The property in a node's metadata
                                                                                    used to determine the address that
                                                                                    the locator binds to for
                                                                                    peer-to-peer communication. If
                                                                                    `None`,the locator uses the value
                                                                                    derived from
                                                                                    ``peer_discovery_address``.
    :ivar str                                               client_bind_address:    The property in a node's metadata
                                                                                    used to determine the address that
                                                                                    the locator binds to for client
                                                                                    communication. If `None`,
                                                                                    the locator uses the node's
                                                                                    hostname. Only takes effect if
                                                                                    ``run_netserver`` is `True`.
    :ivar int                                               client_port:            The port that the locator listens on
                                                                                    for client connections. Only takes
                                                                                    effect if ``run_netserver`` is
                                                                                    `True`.
    :ivar `vas.sqlfire.LocatorInstances.LocatorInstance`    group_instance:         The node instance's group instance
    :ivar str                                               initial_heap:           The initial heap size of the
                                                                                    locator's JVM. If `None` the default
                                                                                    is used.
    :ivar list                                              jvm_options:            The JVM options that are passed to
                                                                                    the locator's JVM when it is started
    :ivar `vas.sqlfire.LocatorNodeLiveConfigurations.LocatorNodeLiveConfigurations`    live_configurations:    The node instance's
                                                                                                                live configuration
    :ivar `vas.sqlfire.LocatorLogs.LocatorLogs`             logs:                   The instance's logs
    :ivar str                                               max_heap:               The max heap size of the locator's
                                                                                    JVM. If `None` the default is used.
    :ivar str                                               name:                   The instance's name
    :ivar `vas.sqlfire.Nodes.Node`                          node:                   The node that contains this instance
    :ivar str                                               peer_discovery_address: The property in a node's metadata
                                                                                    used to determine the address that
                                                                                    the locator binds to for
                                                                                    peer-discovery communication. If
                                                                                    `None`, the locator uses
                                                                                    ``0.0.0.0``.
    :ivar port                                              peer_discovery_port:    The port that the locator listens on
                                                                                    for peer-discovery connections
    :ivar bool                                              run_netserver:          `True` if the locator runs a
                                                                                    netserver that can service thin
                                                                                    clients, otherwise `False`.
    :ivar `vas.shared.Security.Security`                    security:               The resource's security
    :ivar str                                               state:                  Retrieves the state of the resource
                                                                                    from the server. Will be one of:

                                                                                    * ``STARTING``
                                                                                    * ``STARTED``
                                                                                    * ``STOPPING``
                                                                                    * ``STOPPED``
    """

    @property
    def bind_address(self):
        return self.__bind_address

    @property
    def client_bind_address(self):
        return self.__client_bind_address

    @property
    def client_port(self):
        return self.__client_port

    @property
    def initial_heap(self):
        return self.__initial_heap

    @property
    def jvm_options(self):
        return self.__jvm_options

    @property
    def max_heap(self):
        return self.__max_heap

    @property
    def peer_discovery_address(self):
        return self.__peer_discovery_address

    @property
    def peer_discovery_port(self):
        return self.__peer_discovery_port

    @property
    def run_netserver(self):
        return self.__run_netserver

    def __init__(self, client, location):
        super(LocatorNodeInstance, self).__init__(client, location, Node, LocatorLogs, LocatorInstance,
            'locator-group-instance', LocatorNodeLiveConfigurations)

    def reload(self):
        """Reloads the locator node instance's details from the server"""

        super(LocatorNodeInstance, self).reload()

        self.__bind_address = self._details['bind-address']
        self.__client_bind_address = self._details['client-bind-address']
        self.__client_port = self._details['client-port']
        self.__initial_heap = self._details['initial-heap']
        self.__jvm_options = self._details['jvm-options']
        self.__max_heap = self._details['max-heap']
        self.__peer_discovery_address = self._details['peer-discovery-address']
        self.__peer_discovery_port = self._details['peer-discovery-port']
        self.__run_netserver = self._details['run-netserver']

    def __str__(self):
        return "<{} name={} bind_address={} client_bind_address={} client_port={} initial_heap={} jvm_options={} max_heap={} peer_discovery_address={} peer_discovery_port={} run_netserver={}>".format(
            self.__class__, self.name, self.__bind_address, self.__client_bind_address, self.__client_port,
            self.__initial_heap, self.__jvm_options, self.__max_heap, self.__peer_discovery_address,
            self.__peer_discovery_port, self.__run_netserver)


from vas.sqlfire.LocatorInstances import LocatorInstance
from vas.sqlfire.LocatorLogs import LocatorLogs
from vas.sqlfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfigurations
from vas.sqlfire.Nodes import Node
