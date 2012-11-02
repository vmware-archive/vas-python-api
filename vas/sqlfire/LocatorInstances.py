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


from vas.shared.Instance import Instance
from vas.shared.MutableCollection import MutableCollection

class LocatorInstances(MutableCollection):
    """Used to enumerate, create, and delete locator instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorInstances, self).__init__(client, location, 'locator-group-instances', LocatorInstance)

    def create(self, installation, name, bind_address=None, client_bind_address=None, client_port=None,
               initial_heap=None, jvm_options=None, max_heap=None, peer_discovery_address=None,
               peer_discovery_port=None, run_netserver=None):
        """Creates a new locator instance

        :param `vas.sqlfire.Installations.Installation` installation:           The installation that the instance will
                                                                                use
        :param str                                      name:                   The name of the instance
        :param str                                      bind_address:           The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for peer-to-peer
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use the value derived from
                                                                                ``peer-discovery-address``.
        :param str                                      client_bind_address:    The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for client
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use the node's hostname. Only takes
                                                                                effect if ``run-netserver`` is `True`.
        :param int                                      client_port:            The port that the locator listens on for
                                                                                client connections. Only takes effect if
                                                                                ``run-netserver`` is `True`.
        :param str                                      initial_heap:           The initial heap size to be used by the
                                                                                locator's JVM. If not specified, the
                                                                                JVM's default is used.
        :param list                                     jvm_options:            The JVM options that are passed to the
                                                                                locator's JVM when it is started
        :param str                                      max_heap:               The maximum heap size to be used by the
                                                                                locator's JVM. If not specified, the
                                                                                JVM's default is used.
        :param str                                      peer_discovery_address: The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for peer-discovery
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use ``0.0.0.0``.
        :param int                                      peer_discovery_port:    The port that the locator listens on for
                                                                                peer-discovery connections. If omitted,
                                                                                the locator will listen on the default
                                                                                port (10334).
        :param bool                                     run_netserver:          Whether the locator should run a
                                                                                netserver that can service thin clients.
                                                                                Default is `True`.
        :rtype:     :class:`vas.sqlfire.LocatorInstances.LocatorInstance`
        :return:    The new instance
        """

        payload = {'installation': installation._location, 'name': name}

        if bind_address:
            payload['bind-address'] = bind_address

        if client_bind_address:
            payload['client-bind-address'] = client_bind_address

        if client_port is not None:
            payload['client-port'] = client_port

        if initial_heap:
            payload['initial-heap'] = initial_heap

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        if max_heap:
            payload['max-heap'] = max_heap

        if peer_discovery_address:
            payload['peer-discovery-address'] = peer_discovery_address

        if peer_discovery_port is not None:
            payload['peer-discovery-port'] = peer_discovery_port

        if run_netserver is not None:
            payload['run-netserver'] = run_netserver

        return self._create(payload, 'locator-group-instance')


class LocatorInstance(Instance):
    """A locator instance

    :ivar str                                       bind_address:           The property in a node's metadata used to
                                                                            determine the address that the locator binds
                                                                            to for peer-to-peer communication. If
                                                                            `None`,the locator uses the value derived
                                                                            from ``peer_discovery_address``.
    :ivar str                                       client_bind_address:    The property in a node's metadata used to
                                                                            determine the address that the locator binds
                                                                            to for client communication. If `None`, the
                                                                            locator uses the node's hostname. Only takes
                                                                            effect if ``run_netserver`` is `True`.
    :ivar int                                       client_port:            The port that the locator listens on for
                                                                            client connections. Only takes effect if
                                                                            ``run_netserver`` is `True`.
    :ivar `vas.sqlfire.Groups.Group`                group:                  The group that contains this instance
    :ivar `vas.sqlfire.Installations.Installation`  installation:           The installation that this instance is using
    :ivar str                                       initial_heap:           The initial heap size of the locator's JVM.
                                                                            If `None` the default is used.
    :ivar list                                      jvm_options:            The JVM options that are passed to the
                                                                            locator's JVM when it is started
    :ivar `vas.sqlfire.LocatorLiveConfigurations.LocatorLiveConfigurations` live_configurations:    The instance's live
                                                                                                    configurations
    :ivar str                                       max_heap:               The max heap size of the locator's JVM. If
                                                                            `None` the default is used.
    :ivar str                                       name:                   The instance's name
    :ivar list                                      node_instances:         The instance's individual node instances
    :ivar str                                       peer_discovery_address: The property in a node's metadata used to
                                                                            determine the address that the locator binds
                                                                            to for peer-discovery communication. If
                                                                            `None`, the locator uses ``0.0.0.0``.
    :ivar port                                      peer_discovery_port:    The port that the locator listens on for
                                                                            peer-discovery connections
    :ivar `vas.sqlfire.LocatorPendingConfigurations.LocatorPendingConfigurations`   pending_configurations: The instance's
                                                                                                            pending configurations
    :ivar bool                                      run_netserver:          `True` if the locator runs a netserver that
                                                                            can service thin clients, otherwise `False`.
    :ivar `vas.shared.Security.Security`            security:               The resource's security
    :ivar str                                       state:                  Retrieves the state of the resource from the
                                                                            server. Will be one of:

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
        super(LocatorInstance, self).__init__(client, location, Group, Installation, LocatorLiveConfigurations,
            LocatorPendingConfigurations, LocatorNodeInstance, 'locator-node-instance')

    def reload(self):
        """Reloads the locator instance's details from the server"""

        super(LocatorInstance, self).reload()

        self.__bind_address = self._details['bind-address']
        self.__client_bind_address = self._details['client-bind-address']
        self.__client_port = self._details['client-port']
        self.__initial_heap = self._details['initial-heap']
        self.__jvm_options = self._details['jvm-options']
        self.__max_heap = self._details['max-heap']
        self.__peer_discovery_address = self._details['peer-discovery-address']
        self.__peer_discovery_port = self._details['peer-discovery-port']
        self.__run_netserver = self._details['run-netserver']

    def update(self, installation=None, bind_address=None, client_bind_address=None, client_port=None,
               initial_heap=None, jvm_options=None,
               max_heap=None, peer_discovery_address=None, peer_discovery_port=None, run_netserver=None):
        """Updates the locator instance

        :param `vas.sqlfire.Installations.Installation` installation:           The installation that the instance will
                                                                                use
        :param str                                      bind_address:           The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for peer-to-peer
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use the value derived from
                                                                                ``peer-discovery-address``.
        :param str                                      client_bind_address:    The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for client
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use the node's hostname. Only takes
                                                                                effect if ``run-netserver`` is `True`.
        :param int                                      client_port:            The port that the locator listens on for
                                                                                client connections. Only takes effect if
                                                                                ``run-netserver`` is `True`.
        :param str                                      initial_heap:           The initial heap size to be used by the
                                                                                locator's JVM. If not specified, the
                                                                                JVM's default is used.
        :param list                                     jvm_options:            The JVM options that are passed to the
                                                                                locator's JVM when it is started
        :param str                                      max_heap:               The maximum heap size to be used by the
                                                                                locator's JVM. If not specified, the
                                                                                JVM's default is used.
        :param str                                      peer_discovery_address: The property in a node's metadata to use
                                                                                to determine the address that the
                                                                                locator binds to for peer-discovery
                                                                                communication. If omitted, or if the
                                                                                property does not exist, the locator
                                                                                will use ``0.0.0.0``.
        :param int                                      peer_discovery_port:    The port that the locator listens on for
                                                                                peer-discovery connections. If omitted,
                                                                                the locator will listen on the default
                                                                                port (10334).
        :param bool                                     run_netserver:          Whether the locator should run a
                                                                                netserver that can service thin clients.
                                                                                Default is `True`.
        :rtype:     :class:`vas.sqlfire.LocatorInstances.LocatorInstance`
        :return:    The new instance
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

        if initial_heap:
            payload['initial-heap'] = initial_heap

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        if max_heap:
            payload['max-heap'] = max_heap

        if peer_discovery_address:
            payload['peer-discovery-address'] = peer_discovery_address

        if peer_discovery_port is not None:
            payload['peer-discovery-port'] = peer_discovery_port

        if run_netserver is not None:
            payload['run-netserver'] = run_netserver

        self._client.post(self._location, payload)
        self.reload()

    def __str__(self):
        return "<{} name={} bind_address={} client_bind_address={} client_port={} initial_heap={} jvm_options={} max_heap={} peer_discovery_address={} peer_discovery_port={} run_netserver={}>".format(
            self.__class__, self.name, self.__bind_address, self.__client_bind_address, self.__client_port,
            self.__initial_heap, self.__jvm_options, self.__max_heap, self.__peer_discovery_address,
            self.__peer_discovery_port, self.__run_netserver)


from vas.sqlfire.Groups import Group
from vas.sqlfire.Installations import Installation
from vas.sqlfire.LocatorLiveConfigurations import LocatorLiveConfigurations
from vas.sqlfire.LocatorNodeInstances import LocatorNodeInstance
from vas.sqlfire.LocatorPendingConfigurations import LocatorPendingConfigurations
