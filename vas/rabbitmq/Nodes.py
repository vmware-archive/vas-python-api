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
    """Used to enumerate RabbitMQ nodes

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Nodes, self).__init__(client, location, 'nodes', Node)


class Node(GroupableNode):
    """A RabbitMQ node

    :ivar str                                           agent_home:         The location of the vFabric Administration
                                                                            Agent
    :ivar str                                           architecture:       The architecture of the node's operating
                                                                            system
    :ivar list                                          groups:             The groups that contain this node
    :ivar list                                          host_names:         The node's host names
    :ivar `vas.rabbitmq.NodeInstances.NodeInstances`    instances:          The node's instances
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
        self.__instances = self.__instances or NodeInstances(self._client, self.__instances_location)
        return self.__instances


    def __init__(self, client, location):
        super(Node, self).__init__(client, location, Group)
        self.__instances_location = LinkUtils.get_link_href(self._details, 'node-instances')

    def __str__(self):
        return "<{} host_names={} ip_addresses={} ipv4_addresses={} ipv6_addresses={} operating_system={} architecture={} agent_home={} metadata={}>".format(
            self.__class__.__name__, self.host_names, self.ip_addresses, self.ipv4_addresses, self.ipv6_addresses,
            self.operating_system, self.architecture, self.agent_home, self.metadata)


from vas.rabbitmq.Groups import Group
from vas.rabbitmq.NodeInstances import NodeInstances
