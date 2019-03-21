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


from vas.shared.Instance import Instance
from vas.shared.MutableCollection import MutableCollection

class ServerInstances(MutableCollection):
    """Used to enumerate, create, and delete server instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(ServerInstances, self).__init__(client, location, 'server-group-instances', ServerInstance)

    def create(self, installation, name, bind_address=None, client_bind_address=None, client_port=None,
               critical_heap_percentage=None, initial_heap=None, jvm_options=None, max_heap=None, run_netserver=None):
        """Creates a new server instance

        :param `vas.sqlfire.Installations.Installation` installation:               The installation that the instance
                                                                                    will use
        :param str                                      name:                       The name of the instance
        :param str                                      bind_address:               The property in a node's metadata to
                                                                                    use to determine the address that
                                                                                    the server binds to for peer-to-peer
                                                                                    communication. If omitted, or if the
                                                                                    property does not exist, the server
                                                                                    will use the node's hostname.
        :param str                                      client_bind_address:        The property in a node's metadata to
                                                                                    use to determine the address that
                                                                                    the server binds to for client
                                                                                    communication. If omitted, or if the
                                                                                    property does not exist, the server
                                                                                    will use the node's hostname. Only
                                                                                    takes effect if ``run-netserver`` is
                                                                                    `True`.
        :param int                                      client_port:                The port that the server listens on
                                                                                    for client connections. Only takes
                                                                                    effect if ``run-netserver`` is
                                                                                    `True`.
        :param int                                      critical_heap_percentage:   Critical heap threshold as a
                                                                                    percentage of the old generation
                                                                                    heap
        :param str                                      initial_heap:               The initial heap size to be used by
                                                                                    the server's JVM. If not specified,
                                                                                    the JVM's default is used
        :param list                                     jvm_options:                The JVM options that are passed to
                                                                                    the server's JVM when it is started
        :param str                                      max_heap:                   The maximum heap size to be used by
                                                                                    the server's JVM. If not specified,
                                                                                    the JVM's default is used
        :param bool                                     run_netserver:              Whether the locator should run a
                                                                                    netserver that can service thin
                                                                                    clients. Default is `True`.
        :rtype:     :class:`vas.sqlfire.ServerInstances.ServerInstance`
        :return:    The new server instance
        """

        payload = {'installation': installation._location, 'name': name}

        if bind_address:
            payload['bind-address'] = bind_address

        if client_bind_address:
            payload['client-bind-address'] = client_bind_address

        if client_port is not None:
            payload['client-port'] = client_port

        if critical_heap_percentage:
            payload['critical-heap-percentage'] = critical_heap_percentage

        if initial_heap:
            payload['initial-heap'] = initial_heap

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        if max_heap:
            payload['max-heap'] = max_heap

        if run_netserver is not None:
            payload['run-netserver'] = run_netserver

        return self._create(payload, 'server-group-instance')


class ServerInstance(Instance):
    """A server instance

    :ivar str                                       bind_address:               The property in a node's metadata used
                                                                                to determine the address that the server
                                                                                binds to for peer-to-peer communication.
                                                                                If `None`, the server uses the node's
                                                                                hostname.
    :ivar str                                       client_bind_address:        the property in a node's metadata used
                                                                                to determine the address that the server
                                                                                binds to for client communication. If
                                                                                `None`, the server uses localhost. Only
                                                                                takes effect if ``run_netserver`` is
                                                                                `True`.
    :ivar int                                       client_port:                the port that the server listens on for
                                                                                client connections. Only takes effect if
                                                                                ``run_netserver`` is `True`.
    :ivar int                                       critical_heap_percentage:   Critical heap percentage as a percentage
                                                                                of the old generation heap. If `None`
                                                                                the server uses the default.
    :ivar `vas.sqlfire.Groups.Group`                group:                      The group that contains this instance
    :ivar str                                       initial_heap:               The initial heap size of the server's
                                                                                JVM. If `None` the default is used.
    :ivar `vas.sqlfire.Installations.Installation`  installation:               The installation that this instance is
                                                                                using
    :ivar list                                      jvm_options:                The JVM options that are passed to the
                                                                                server's JVM when it is started
    :ivar `vas.sqlfire.ServerLiveConfigurations.ServerLiveConfigurations`   live_configurations:    The instance's live
                                                                                                    configurations
    :ivar str                                       max_heap:                   The max heap size of the server's JVM.
                                                                                If `None` the default is used.
    :ivar str                                       name:                       The instance's name
    :ivar list                                      node_instances:             The instance's individual node instances
    :ivar `vas.sqlfire.ServerPendingConfigurations.ServerPendingConfigurations` pending_configurations: The instance's
                                                                                                        pending configurations
    :ivar bool                                      run_netserver:              `True` if the server runs a netserver
                                                                                that can service thin clients, otherwise
                                                                                `False`
    :ivar `vas.shared.Security.Security`            security:                   The resource's security
    :ivar str                                       state:                      Retrieves the state of the resource from
                                                                                the server. Will be one of:

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
        super(ServerInstance, self).__init__(client, location, Group, Installation, ServerLiveConfigurations,
            ServerPendingConfigurations, ServerNodeInstance, 'server-node-instance')

    def reload(self):
        """Reloads the instance's details from the server"""

        super(ServerInstance, self).reload()

        self.__bind_address = self._details['bind-address']
        self.__client_bind_address = self._details['client-bind-address']
        self.__client_port = self._details['client-port']
        self.__critical_heap_percentage = self._details['critical-heap-percentage']
        self.__initial_heap = self._details['initial-heap']
        self.__jvm_options = self._details['jvm-options']
        self.__max_heap = self._details['max-heap']
        self.__run_netserver = self._details['run-netserver']

    def update(self, installation=None, bind_address=None, client_bind_address=None, client_port=None,
               critical_heap_percentage=None, initial_heap=None, jvm_options=None, max_heap=None, run_netserver=None):
        """Updates the instance

        :param `vas.sqlfire.Installations.Installation` installation:               The installation that the instance
                                                                                    will use
        :param str                                      bind_address:               The property in a node's metadata to
                                                                                    use to determine the address that
                                                                                    the server binds to for peer-to-peer
                                                                                    communication. If omitted, or if the
                                                                                    property does not exist, the server
                                                                                    will use the node's hostname.
        :param str                                      client_bind_address:        The property in a node's metadata to
                                                                                    use to determine the address that
                                                                                    the server binds to for client
                                                                                    communication. If omitted, or if the
                                                                                    property does not exist, the server
                                                                                    will use the node's hostname. Only
                                                                                    takes effect if ``run-netserver`` is
                                                                                    `True`.
        :param int                                      client_port:                The port that the server listens on
                                                                                    for client connections. Only takes
                                                                                    effect if ``run-netserver`` is
                                                                                    `True`.
        :param int                                      critical_heap_percentage:   Critical heap threshold as a
                                                                                    percentage of the old generation
                                                                                    heap
        :param str                                      initial_heap:               The initial heap size to be used by
                                                                                    the server's JVM. If not specified,
                                                                                    the JVM's default is used
        :param list                                     jvm_options:                The JVM options that are passed to
                                                                                    the server's JVM when it is started
        :param str                                      max_heap:                   The maximum heap size to be used by
                                                                                    the server's JVM. If not specified,
                                                                                    the JVM's default is used
        :param bool                                     run_netserver:              Whether the locator should run a
                                                                                    netserver that can service thin
                                                                                    clients. Default is `True`.
        :rtype:     :class:`vas.sqlfire.ServerInstances.ServerInstance`
        :return:    The new server instance
        """

        payload = {}

        if installation:
            payload['installation'] = installation._location

        if bind_address:
            payload['bind-address'] = bind_address

        if client_bind_address:
            payload['client-bind-address'] = client_bind_address

        if client_port is not None:
            payload['client-port'] = client_port

        if critical_heap_percentage:
            payload['critical-heap-percentage'] = critical_heap_percentage

        if initial_heap:
            payload['initial-heap'] = initial_heap

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        if max_heap:
            payload['max-heap'] = max_heap

        if run_netserver is not None:
            payload['run-netserver'] = run_netserver

        self._client.post(self._location, payload)
        self.reload()

    def __str__(self):
        return "<{} name={} bind_address={} client_bind_address={} client_port={} critical_heap_percentage={} initial_heap={} jvm_options={} max_heap={} run_netserver={}>".format(
            self.__class__, self.name, self.__bind_address, self.__client_bind_address, self.__client_port,
            self.__critical_heap_percentage, self.__initial_heap, self.__jvm_options, self.__max_heap,
            self.__run_netserver)


from vas.sqlfire.Groups import Group
from vas.sqlfire.Installations import Installation
from vas.sqlfire.ServerLiveConfigurations import ServerLiveConfigurations
from vas.sqlfire.ServerNodeInstances import ServerNodeInstance
from vas.sqlfire.ServerPendingConfigurations import ServerPendingConfigurations
