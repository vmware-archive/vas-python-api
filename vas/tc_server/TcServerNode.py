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

class TcServerNode(Node):
    """A tc Server node

    :ivar str agent_home:   The path that the agent is installed at on the node
    :ivar str architecture: The operating system architecture of the node
    :ivar list groups: The The :class:`vas.tc_server.TcServerGroup` s that this node is a member of
    :ivar list host_names:  The host names configured on the node
    :ivar list ip_addresses:    The ip addresses the node listens on
    :ivar str java_home:    The path for the ``$JAVA_HOME`` that the agent is using
    :ivar dict metadata:    Arbitrary metadata configured in the ``agent.properties`` file on the node
    :ivar `vas.tc_server.TcServerNodeInstances` instances: The collection of node instances
    :ivar str operating_system: The operating system of the node
    :ivar `vas.shared.Security` security:   The security configuration for the node
    """

    __KEY_JAVA_HOME = 'java-home'

    __REL_GROUP = 'group'

    __REL_NODE_INSTANCES = 'node-instances'

    def __init__(self, client, location):
        super(TcServerNode, self).__init__(client, location)

        self.java_home = self._details[self.__KEY_JAVA_HOME]
        self.instances = TcServerNodeInstances(self._client, self._links[self.__REL_NODE_INSTANCES][0])

    @property
    def groups(self):
        return [TcServerGroup(self._client, group_location) for group_location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_GROUP)]

from vas.tc_server.TcServerGroup import TcServerGroup
from vas.tc_server.TcServerNodeInstances import TcServerNodeInstances
