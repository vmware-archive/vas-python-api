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

class VFabricNode(Node):
    """A vFabric node

    :ivar str agent_home:   The path that the agent is installed at on the node
    :ivar str architecture: The operating system architecture of the node
    :ivar list host_names:  The host names configured on the node
    :ivar list ip_addresses:    The ip addresses the node listens on
    :ivar dict metadata:    Arbitrary metadata configured in the ``agent.properties`` file on the node
    :ivar str operating_system: The operating system of the node
    :ivar `vas.shared.Security` security:   The security configuration for the node
    """

    pass
