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


from vas.shared.Node import Node
from vas.util.LinkUtils import LinkUtils

class GemFireNode(Node):
    """A GemFire node

    :ivar str agent_home:   The path that the agent is installed at on the node
    :ivar str architecture: The operating system architecture of the node
    :ivar list groups: The The :class:`vas.gemfire.GemFireGroup` s that this node is a member of
    :ivar list host_names:  The host names configured on the node
    :ivar list ip_addresses:    The ip addresses the node listens on
    :ivar str java_home:    The path for the ``$JAVA_HOME`` that the agent is using
    :ivar dict metadata:    Arbitrary metadata configured in the ``agent.properties`` file on the node
    :ivar `vas.gemfire.GemFireAgentNodeInstances` agent_instances: The collection of node agent instances
    :ivar `vas.gemfire.GemFireCacheServerNodeInstances` cache_server_instances: The collection of node cache server instances
    :ivar `vas.gemfire.GemFireLocatorNodeInstances` locator_instance: The collection of node locator instances
    :ivar str operating_system: The operating system of the node
    :ivar `vas.shared.Security` security:   The security configuration for the node
    """

    __KEY_JAVA_HOME = 'java-home'

    __REL_GROUP = 'group'

    __REL_AGENT_NODE_INSTANCES = 'agent-node-instances'

    __REL_CACHE_SERVER_NODE_INSTANCES = 'cache-server-node-instances'

    __REL_LOCATOR_NODE_INSTANCES = 'locator-node-instances'

    def __init__(self, client, location):
        super(GemFireNode, self).__init__(client, location)

        self.java_home = self._details[self.__KEY_JAVA_HOME]
        self.agent_instances = GemFireAgentNodeInstances(self._client, self._links[self.__REL_AGENT_NODE_INSTANCES][0])
        self.cache_server_instances = GemFireCacheServerNodeInstances(self._client,
            self._links[self.__REL_CACHE_SERVER_NODE_INSTANCES][0])
        self.locator_instances = GemFireLocatorNodeInstances(self._client,
            self._links[self.__REL_LOCATOR_NODE_INSTANCES][0])

    @property
    def groups(self):
        return [GemFireGroup(self._client, group_location) for group_location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_GROUP)]

from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireAgentNodeInstances import GemFireAgentNodeInstances
from vas.gemfire.GemFireCacheServerNodeInstances import GemFireCacheServerNodeInstances
from vas.gemfire.GemFireLocatorNodeInstances import GemFireLocatorNodeInstances
