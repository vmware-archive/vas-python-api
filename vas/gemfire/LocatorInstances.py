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

class LocatorInstances(MutableCollection):
    """Used to enumerate, create, and delete locator instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorInstances, self).__init__(client, location, 'locator-group-instances', LocatorInstance)

    def create(self, installation, name, address=None, peer=None, port=None, server=None):
        """Creates a new locator instance

        :param `vas.gemfire.Installations.Installation` installation:   The installation that the instance will use
        :param str                                      name:           The name of the locator group instance
        :param str                                      address:        The property in a node's metadata to use to
                                                                        determine the address that the locator instance
                                                                        will bind to. If omitted or null, the
                                                                        configuration will not be changed. If an empty
                                                                        string is specified, the locator instance will
                                                                        bind to the default network address.
        :param bool                                     peer:           `True` if the locator should act as a peer,
                                                                        otherwise `False`
        :param int                                      port:           The port that the locator will listen on
        :param bool                                     server:         `True` if the locator should act as a server,
                                                                        otherwise `False`
        :rtype:         :class:`vas.gemfire.LocatorInstances.LocatorInstance`
        :return:        The new instance
        """

        payload = {'installation': installation._location, 'name': name}

        if address:
            payload['address'] = address

        if peer is not None:
            payload['peer'] = peer

        if port:
            payload['port'] = port

        if server is not None:
            payload['server'] = server

        return self._create(payload, 'locator-group-instance')


class LocatorInstance(Instance):
    """A locator instance

    :ivar str                                       address:        The address of the network card on which the locator
                                                                    will listen
    :ivar `vas.gemfire.Groups.Group`                group:          The group that contains this instance
    :ivar `vas.gemfire.Installations.Installation`  installation:   The installation that this instance is using
    :ivar `vas.gemfire.LocatorLiveConfigurations.LocatorLiveConfigurations` live_configurations:    The instance's live configurations
    :ivar str                                       name:           The instance's name
    :ivar list                                      node_instances: The instance's individual node instances
    :ivar bool                                      peer:           `True` if the locator should act as a peer,
                                                                    otherwise `False`
    :ivar `vas.gemfire.LocatorPendingConfigurations.LocatorPendingConfigurations`   pending_configurations: The instance's pending
                                                                                            configurations
    :ivar int                                       port:           The port that the locator will listen on
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar bool                                      server:         `True` if the locator should act as a server,
                                                                    otherwise `False`
    :ivar str                                       state:          Retrieves the state of the resource from the server.
                                                                    Will be one of:

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
        super(LocatorInstance, self).__init__(client, location, Group, Installation, LocatorLiveConfigurations,
            LocatorPendingConfigurations, LocatorNodeInstance, 'locator-node-instance')

    def reload(self):
        """Reloads the instance's details from the server"""

        super(LocatorInstance, self).reload()

        self.__address = self._details['address']
        self.__peer = self._details['peer']
        self.__port = self._details['port']
        self.__server = self._details['server']

    def update(self, installation=None, address=None, peer=None, port=None, server=None):
        """Updates the instance using the supplied ``options``

        :param `vas.gemfire.Installations.Installation` installation:   The installation to be used by the instance. If
                                                                        omitted or `None`, the installation
                                                                        configuration will not be changed.
        :param str                                      address:        The property in a node's metadata to use to
                                                                        determine the address that the locator instance
                                                                        will bind to. If omitted or null, the
                                                                        configuration will not be changed. If an empty
                                                                        string is specified, the locator instance will
                                                                        bind to the default network address. If omitted
                                                                        or `None`, the address configuration will not be
                                                                        changed.
        :param bool                                     peer:           `True` if the locator should act as a peer,
                                                                        otherwise `False`. If omitted or `None`, the
                                                                        peer configuration will not be changed.
        :param int                                      port:           The port that the locator will listen on. If
                                                                        omitted or `None`, the port configuration will
                                                                        not be changed
        :param bool                                     server:        `True` if the locator should act as a server,
                                                                        otherwise `False`. If omitted or `None`, the
                                                                        server configuration will not be changed.
        """

        payload = {}

        if installation:
            payload['installation'] = installation._location

        if address:
            payload['address'] = address

        if peer is not None:
            payload['peer'] = peer

        if port:
            payload['port'] = port

        if server is not None:
            payload['server'] = server

        self._client.post(self._location, payload)
        self.reload()

    def __str__(self):
        return "<{} name={} port={} peer={} server={} address={}>".format(self.__class__.__name__, self.name,
            self.__port, self.__peer, self.__server, self.__address)


from vas.gemfire.Groups import Group
from vas.gemfire.Installations import Installation
from vas.gemfire.LocatorLiveConfigurations import LocatorLiveConfigurations
from vas.gemfire.LocatorNodeInstances import LocatorNodeInstance
from vas.gemfire.LocatorPendingConfigurations import LocatorPendingConfigurations
