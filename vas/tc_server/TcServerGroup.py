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


from vas.shared.Group import Group

class TcServerGroup(Group):
    """A tc Server group

    :ivar `vas.tc_server.TcServerGroupInstances` instances:  The collection of instances
    :ivar `vas.tc_server.TcServerInstallations` installations:  The collection of installations
    :ivar str name: The name of the group
    :ivar list nodes: The :class:`vas.tc_server.TcServerNode` s that are members of the group
    :ivar `vas.shared.Security` security:   The security configuration for the group
    """

    __REL_GROUP_INSTANCES = 'group-instances'

    def __init__(self, client, location):
        super(TcServerGroup, self).__init__(client, location)

        self.instances = TcServerGroupInstances(self._client, self._links[self.__REL_GROUP_INSTANCES][0])

    def update(self, nodes):
        """Update the membership of the group

        :type nodes:    :obj:`list` of :class:`vas.tc_server.TcServerNode`
        :param nodes:   The collection of nodes to be included in the group
        """

        self._client.post(self._location_self, {'nodes': [node._location_self for node in nodes]})

    def _create_installations(self, client, location):
        return TcServerInstallations(client, location)

    def _create_node(self, client, location):
        return TcServerNode(client, location)

from vas.tc_server.TcServerInstallations import TcServerInstallations
from vas.tc_server.TcServerGroupInstances import TcServerGroupInstances
from vas.tc_server.TcServerNode import TcServerNode
