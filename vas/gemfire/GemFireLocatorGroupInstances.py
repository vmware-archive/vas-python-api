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


from vas.shared.GroupInstances import GroupInstances

class GemFireLocatorGroupInstances(GroupInstances):
    """An collection of GemFire locator group instances

    :ivar `vas.shared.Security` security:   The security configuration for the collection of locator group instances
    """

    __REL_LOCATOR_GROUP_INSTANCE = 'locator-group-instance'

    __COLLECTION_KEY = 'locator-group-instances'

    def __init__(self, client, location):
        super(GemFireLocatorGroupInstances, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, name, installation, address=None, peer=None, port=None, server=None):
        """Create a new locator group instance

        :type name:     :obj:`str`
        :param name:    The name of the locator group instance
        :type installation:     :class:`vas.gemfire.GemFireInstallation`
        :param installation:    The installation that the locator group instance should use at runtime
        :type address:     :obj:`str`
        :param address:    The name of the property, configured in the ``agent.properties`` file, that will be used to
                           configure the address of the network card on which the locator will listen
        :type peer:     :obj:`bool`
        :param peer:    Whether the locator should act as a peer
        :type port:     :obj:`int`
        :param port:    The port on which the locator should listen on
        :type server:     :obj:`bool`
        :param server:    Whether the locator should act as a server
        :rtype:         :class:`vas.gemfire.GemFireLocatorGroupInstance`
        :return:        The newly created locator group instance
        """

        payload = dict()
        payload['name'] = name
        payload['installation'] = installation._location_self

        if address is not None:
            payload['address'] = address

        if peer is not None:
            payload['peer'] = peer

        if port is not None:
            payload['port'] = port

        if server is not None:
            payload['server'] = server

        location = self._client.post(self._location_self, payload, self.__REL_LOCATOR_GROUP_INSTANCE)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return GemFireLocatorGroupInstance(client, location)

from vas.gemfire.GemFireLocatorGroupInstance import GemFireLocatorGroupInstance
