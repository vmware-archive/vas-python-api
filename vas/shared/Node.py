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


from vas.shared.Type import Type

class Node(Type):
    """An abstract node

    :ivar str agent_home:   The path that the agent is installed at on the node
    :ivar str architecture: The operating system architecture of the node
    :ivar list host_names: The host names configured on the node
    :ivar list ip_addresses: The ip addresses the node listens on
    :ivar dict metadata:    Arbitrary metadata configured in the ``agent.properties`` file on the node
    :ivar str operating_system: The operating system of the node
    :ivar `vas.shared.Security` security:   The security configuration for the node
    """

    __KEY_AGENT_HOME = 'agent-home'

    __KEY_ARCHITECTURE = 'architecture'

    __KEY_HOST_NAMES = 'host-names'

    __KEY_IP_ADDRESSES = 'ip-addresses'

    __KEY_METADATA = 'metadata'

    __KEY_OPERATING_SYSTEM = 'operating-system'

    def __init__(self, client, location):
        super(Node, self).__init__(client, location)

        self.agent_home = self._details[self.__KEY_AGENT_HOME]
        self.architecture = self._details[self.__KEY_ARCHITECTURE]
        self.host_names = self._details[self.__KEY_HOST_NAMES]
        self.ip_addresses = self._details[self.__KEY_IP_ADDRESSES]
        self.metadata = self._details[self.__KEY_METADATA]
        self.operating_system = self._details[self.__KEY_OPERATING_SYSTEM]
