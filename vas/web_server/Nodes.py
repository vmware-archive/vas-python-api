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


from vas.shared.Collection import Collection
from vas.shared.Nodes import GroupableNode
from vas.util.LinkUtils import LinkUtils

class Nodes(Collection):
    """Used to enumerate Web Server nodes

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Nodes, self).__init__(client, location, 'nodes', Node)


class Node(GroupableNode):
    """A Web Server node

    :ivar str                                           agent_home:         The location of the vFabric Administration
                                                                            Agent
    :ivar str                                           architecture:       The architecture of the node's operating
                                                                            system
    :ivar list                                          groups:             The groups that contain this node
    :ivar list                                          host_names:         The node's host names
    :ivar `vas.web_server.NodeInstances.NodeInstances`  instances:          The node's instances
    :ivar list                                          ip_addresses:       The node's IP addresses
    :ivar list                                          ipv4_addresses:     The node's IPv4 addresses
    :ivar list                                          ipv6_addresses:     The node's IPv6 addresses
    :ivar dict                                          metadata:           The node's metadata
    :ivar str                                           operating_system:   The node's operating system
    :ivar `vas.shared.Security.Security`                security:           The resource's security
    """

    __instances = None

    @property
    def instances(self):
        self.__instances = self.__instances or NodeInstances(self._client, self.__node_instances_location)
        return self.__instances


    def __init__(self, client, location):
        super(Node, self).__init__(client, location, Group)

        self.__node_instances_location = LinkUtils.get_link_href(self._details, 'node-instances')


from vas.web_server.Groups import Group
from vas.web_server.NodeInstances import NodeInstances
