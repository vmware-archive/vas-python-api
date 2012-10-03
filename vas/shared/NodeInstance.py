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

class NodeInstance(Type):
    """An abstract node instance

    :ivar `vas.shared.GroupInstance` group_instance: The group instance that the node instance is a member of
    :ivar `vas.shared.Logs` logs: The collection of logs
    :ivar str name: The name of the node instance
    :ivar `vas.shared.Node` node: The node instance's parent node
    :ivar `vas.shared.Security` security:   The security configuration for the node instance
    :ivar str state:    The current state of the node instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __KEY_NAME = 'name'

    __REL_LOGS = 'logs'

    __REL_NODE = 'node'

    __REL_STATE = 'state'

    def __init__(self, client, location, group_instance_rel):
        super(NodeInstance, self).__init__(client, location)

        self._location_state = self._links[self.__REL_STATE][0]

        self.group_instance = self._create_group_instance(client, self._links[group_instance_rel][0])
        self.logs = self._create_logs(client, self._links[self.__REL_LOGS][0])
        self.name = self._details[self.__KEY_NAME]
        self.node = self._create_node(client, self._links[self.__REL_NODE][0])

    def stop(self):
        """Stop the instance by attempting to set its ``status`` to ``STOPPED``"""

        self._client.post(self._location_state, {'status': 'STOPPED'})

    @property
    def state(self):
        return self._client.get(self._location_state)['status']

    def _create_group_instance(self, client, location):
        raise VFabricAdministrationServerError('_create_group_instance(self, client, location) method is unimplemented')

    def _create_logs(self, client, location):
        raise VFabricAdministrationServerError('_create_logs(self, client, location) method is unimplemented')

    def _create_node(self, client, location):
        raise VFabricAdministrationServerError('_create_node(self, client, location) method is unimplemented')
