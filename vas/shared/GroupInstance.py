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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.Type import Type
from vas.util.LinkUtils import LinkUtils

class GroupInstance(Type):
    """An abstract group instance

    :ivar `vas.shared.Group` group: The group instance's parent group
    :ivar `vas.shared.Installation` installation: The group instance's installation
    :ivar `vas.shared.LiveConfigurations` live_configurations:  The collection of live configurations
    :ivar str name: The name of the group instance
    :ivar list node_instances: The :class:`vas.shared.NodeInstance` s that are members of the group instance
    :ivar `vas.shared.PendingConfigurations` pending_configurations:    The collection of pending configurations
    :ivar `vas.shared.Security` security:   The security configuration for the group instance
    :ivar str state:    The current state of the group instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __KEY_NAME = 'name'

    __REL_GROUP = 'group'

    __REL_INSTALLATION = 'installation'

    __REL_LIVE_CONFIGURATIONS = 'live-configurations'

    __REL_PENDING_CONFIGURATIONS = 'pending-configurations'

    __REL_STATE = 'state'

    def __init__(self, client, location, node_instance_rel):
        super(GroupInstance, self).__init__(client, location)

        self.__location_state = self._links[self.__REL_STATE][0]
        self.__node_instance_rel = node_instance_rel

        self.group = self._create_group(client, self._links[self.__REL_GROUP][0])
        self.installation = self._create_installation(client, self._links[self.__REL_INSTALLATION][0])
        self.live_configurations = self._create_live_configurations(client,
            self._links[self.__REL_LIVE_CONFIGURATIONS][0])
        self.name = self._details[self.__KEY_NAME]
        self.pending_configurations = self._create_pending_configurations(client,
            self._links[self.__REL_PENDING_CONFIGURATIONS][0])

    def start(self, serial=False):
        """Start the instance by attempting to set its ``status`` to ``STARTED``

        :type serial:   :obj:`bool`
        :param serial:  Whether to start the group's instances serially
        """

        self._client.post(self.__location_state, {'status': 'STARTED', 'serial': serial})

    def stop(self, serial=False):
        """Stop the instance by attempting to set its ``status`` to ``STOPPED``

        :type serial:   :obj:`bool`
        :param serial:  Whether to stop the group's instances serially
        """

        self._client.post(self.__location_state, {'status': 'STOPPED', 'serial': serial})

    @property
    def state(self):
        return self._client.get(self.__location_state)['status']

    @property
    def nodes_instances(self):
        return [self._create_node_instance(self._client, node_location) for node_location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__node_instance_rel)]

    def _create_group(self, client, location):
        raise VFabricAdministrationServerError('_create_group(self, client, location) method is unimplemented')

    def _create_installation(self, client, location):
        raise VFabricAdministrationServerError('_create_installation(self, client, location) method is unimplemented')

    def _create_live_configurations(self, client, location):
        raise VFabricAdministrationServerError(
            '_create_live_configurations(self, client, location) method is unimplemented')

    def _create_node_instance(self, client, location):
        raise VFabricAdministrationServerError('_create_node_instance(self, client, location) method is unimplemented')

    def _create_pending_configurations(self, client, location):
        raise VFabricAdministrationServerError(
            '_create_pending_configurations(self, client, location) method is unimplemented')
