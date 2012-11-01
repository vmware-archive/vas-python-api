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
from vas.util.LinkUtils import LinkUtils

class ServerNodeInstances(NodeInstances):
    """Used to enumerate server instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(ServerNodeInstances, self).__init__(client, location, 'server-node-instances', ServerNodeInstance)


class ServerNodeInstance(NodeInstance):
    """A server node instance

    :ivar str                                           bind_address:               The property in a node's metadata
                                                                                    used to determine the address that
                                                                                    the server binds to for peer-to-peer
                                                                                    communication. If `None`, the server
                                                                                    uses the node's hostname.
    :ivar str                                           client_bind_address:        the property in a node's metadata
                                                                                    used to determine the address that
                                                                                    the server binds to for client
                                                                                    communication. If `None`, the server
                                                                                    uses localhost. Only takes effect if
                                                                                    ``run_netserver`` is `True`.
    :ivar int                                           client_port:                the port that the server listens on
                                                                                    for client connections. Only takes
                                                                                    effect if ``run_netserver`` is
                                                                                    `True`.
    :ivar int                                           critical_heap_percentage:   Critical heap percentage as a
                                                                                    percentage of the old generation
                                                                                    heap. If `None` the server uses the
                                                                                    default.
    :ivar `vas.sqlfire.ServerInstances.ServerInstance`  group_instance:             The node instance's group instance
    :ivar str                                           initial_heap:               The initial heap size of the
                                                                                    server's JVM. If `None` the default
                                                                                    is used.
    :ivar list                                          jvm_options:                The JVM options that are passed to
                                                                                    the server's JVM when it is started
    :ivar `vas.sqlfire.ServerNodeLiveConfigurations.ServerNodeLiveConfigurations`   live_configurations:    The node instance's
                                                                                                            live configuration
    :ivar `vas.sqlfire.ServerLogs.ServerLogs`           logs:                       The instance's logs
    :ivar str                                           max_heap:                   The max heap size of the server's
                                                                                    JVM. If `None` the default is used.
    :ivar str                                           name:                       The instance's name
    :ivar bool                                          run_netserver:              `True` if the server runs a
                                                                                    netserver that can service thin
                                                                                    clients, otherwise `False`
    :ivar `vas.sqlfire.Nodes.Node`                      node:                       The node that contains this instance
    :ivar `vas.shared.Security.Security`                security:                   The resource's security
    :ivar str                                           state:                      Retrieves the state of the resource
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
    def critical_heap_percentage(self):
        return self.__critical_heap_percentage

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
    def run_netserver(self):
        return self.__run_netserver

    def __init__(self, client, location):
        super(ServerNodeInstance, self).__init__(client, location, Node, ServerLogs, ServerInstance,
            'server-group-instance', ServerNodeLiveConfigurations)

        self.__state_location = LinkUtils.get_link_href(self._details, 'state')

    def reload(self):
        """Reloads the instance's details from the server"""

        super(ServerNodeInstance, self).reload()

        self.__bind_address = self._details['bind-address']
        self.__client_bind_address = self._details['client-bind-address']
        self.__client_port = self._details['client-port']
        self.__critical_heap_percentage = self._details['critical-heap-percentage']
        self.__initial_heap = self._details['initial-heap']
        self.__jvm_options = self._details['jvm-options']
        self.__max_heap = self._details['max-heap']
        self.__run_netserver = self._details['run-netserver']

    def start(self, rebalance=None):
        """Starts the resource

        :param bool rebalance:  Whether to rebalance the server instance on start
        """

        payload = {'status': 'STARTED'}

        if rebalance is not None:
            payload['rebalance'] = rebalance

        self._client.post(self.__state_location, payload)

    def __str__(self):
        return "<{} name={} bind_address={} client_bind_address={} client_port={} critical_heap_percentage={} initial_heap={} jvm_options={} max_heap={} run_netserver={}>".format(
            self.__class__, self.name, self.__bind_address, self.__client_bind_address, self.__client_port,
            self.__critical_heap_percentage, self.__initial_heap, self.__jvm_options, self.__max_heap,
            self.__run_netserver)


from vas.sqlfire.Nodes import Node
from vas.sqlfire.ServerInstances import ServerInstance
from vas.sqlfire.ServerLogs import ServerLogs
from vas.sqlfire.ServerNodeLiveConfigurations import ServerNodeLiveConfigurations
