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

class Group(Type):
    """An abstract group

    :ivar str name: The name of the group
    :ivar `vas.shared.Installations` installations: The collection of installations
    :ivar list nodes: The :class:`vas.shared.Node` s that are members of the group
    :ivar `vas.shared.Security` security:   The security configuration for the group
    """

    __KEY_NAME = 'name'

    __REL_INSTALLATIONS = 'installations'

    __REL_NODE = 'node'

    def __init__(self, client, location):
        super(Group, self).__init__(client, location)

        self.name = self._details[self.__KEY_NAME]
        self.installations = self._create_installations(client, self._links[self.__REL_INSTALLATIONS][0])

    @property
    def nodes(self):
        return [self._create_node(self._client, node_location) for node_location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_NODE)]

    def _create_installations(self, client, location):
        raise VFabricAdministrationServerError('_create_installations(self, client, location) method is unimplemented')

    def _create_node(self, client, location):
        raise VFabricAdministrationServerError('_create_node(self, client, location) method is unimplemented')
