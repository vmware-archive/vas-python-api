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

class GemFireGroup(Group):
    """A GemFire group

    :ivar `vas.gemfire.GemFireAgentGroupInstances` agent_instances:  The collection of agent instances
    :ivar `vas.gemfire.GemFireCacheServerGroupInstances` cache_server_instances:  The collection of cache server instances
    :ivar `vas.gemfire.GemFireInstallations` installations:  The collection of installations
    :ivar `vas.gemfire.GemFireLocatorGroupInstances` locator_instances:  The collection of locator instances
    :ivar str name: The name of the group
    :ivar list nodes: The :class:`vas.gemfire.GemFireNode` s that are members of the group
    :ivar `vas.shared.Security` security:   The security configuration for the group
    """

    __REL_AGENT_GROUP_INSTANCES = 'agent-group-instances'

    __REL_CACHE_SERVER_GROUP_INSTANCES = 'cache-server-group-instances'

    __REL_LOCATOR_GROUP_INSTANCES = 'locator-group-instances'

    def __init__(self, client, location):
        super(GemFireGroup, self).__init__(client, location)

        self.agent_instances = GemFireAgentGroupInstances(self._client, self._links[self.__REL_AGENT_GROUP_INSTANCES][0])
        self.cache_server_instances = GemFireCacheServerGroupInstances(self._client, self._links[self.__REL_CACHE_SERVER_GROUP_INSTANCES][0])
        self.locator_instances = GemFireLocatorGroupInstances(self._client, self._links[self.__REL_LOCATOR_GROUP_INSTANCES][0])

    def update(self, nodes):
        """Update the membership of the group

        :type nodes:    :obj:`list` of :class:`vas.gemfire.GemFireNode`
        :param nodes:   The collection of nodes to be included in the group
        """

        self._client.post(self._location_self, {'nodes': [node._location_self for node in nodes]})

    def _create_installations(self, client, location):
        return GemFireInstallations(client, location)

    def _create_node(self, client, location):
        return GemFireNode(client, location)

from vas.gemfire.GemFireInstallations import GemFireInstallations
from vas.gemfire.GemFireAgentGroupInstances import GemFireAgentGroupInstances
from vas.gemfire.GemFireCacheServerGroupInstances import GemFireCacheServerGroupInstances
from vas.gemfire.GemFireLocatorGroupInstances import GemFireLocatorGroupInstances
from vas.gemfire.GemFireNode import GemFireNode
