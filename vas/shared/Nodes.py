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


from vas.shared.Resource import Resource

class Node(Resource):
    """A node, i.e. a machine with the vFabric Administration agent installed on it

    :ivar str                               agent_home:         The location of the vFabric Administration Agent
    :ivar str                               architecture:       The architecture of the node's operating system
    :ivar list                              host_names:         The node's host names
    :ivar list                              ip_addresses:       The node's IP addresses
    :ivar list                              ipv4_addresses:     The node's IPv4 addresses
    :ivar list                              ipv6_addresses:     The node's IPv6 addresses
    :ivar dict                              metadata:           The node's metadata
    :ivar str                               operating_system:   The node's operating system
    :ivar `vas.shared.Security.Security`    security:           The resource's security
    """

    @property
    def agent_home(self):
        return self.__agent_home

    @property
    def architecture(self):
        return self.__architecture

    @property
    def host_names(self):
        return self.__host_names

    @property
    def ip_addresses(self):
        return self.__ip_addresses

    @property
    def ipv4_addresses(self):
        return self.__ipv4_addresses

    @property
    def ipv6_addresses(self):
        return self.__ipv6_addresses

    @property
    def metadata(self):
        return self.__metadata

    @property
    def operating_system(self):
        return self.__operating_system

    def reload(self):
        """Reloads the node's details from the server"""

        super(Node, self).reload()
        self.__agent_home = self._details['agent-home']
        self.__architecture = self._details['architecture']
        self.__host_names = self._details['host-names']
        self.__ip_addresses = self._details['ip-addresses']

        if 'ipv4-addresses' in self._details:
            self.__ipv4_addresses = self._details['ipv4-addresses']

        if 'ipv6-addresses' in self._details:
            self.__ipv6_addresses = self._details['ipv6-addresses']

        self.__metadata = self._details['metadata']
        self.__operating_system = self._details['operating-system']


    def update(self, metadata):
        """Updates the node's metadata

        :param dict metadata:   The node's new metadata
        """

        self._client.post(self._location, {'metadata': metadata})
        self.reload()


class GroupableNode(Node):
    """A node that can be grouped

    :ivar str                               agent_home:         The location of the vFabric Administration Agent
    :ivar str                               architecture:       The architecture of the node's operating system
    :ivar list                              groups:             The groups that contain this node
    :ivar list                              host_names:         The node's host names
    :ivar list                              ip_addresses:       The node's IP addresses
    :ivar list                              ipv4_addresses:     The node's IPv4 addresses
    :ivar list                              ipv6_addresses:     The node's IPv6 addresses
    :ivar dict                              metadata:           The node's metadata
    :ivar str                               operating_system:   The node's operating system
    :ivar `vas.shared.Security.Security`    security:           The resource's security
    """

    @property
    def groups(self):
        self.__groups = self.__groups or self._create_resources_from_links('group', self.__group_class)
        return self.__groups

    def __init__(self, client, location, group_class):
        super(GroupableNode, self).__init__(client, location)
        self.__group_class = group_class

    def reload(self):
        """Reloads the node's details from the server"""

        super(GroupableNode, self).reload()
        self.__groups = None

