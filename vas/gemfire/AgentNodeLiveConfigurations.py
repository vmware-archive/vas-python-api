# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.shared.Collection import Collection
from vas.shared.NodeConfiguration import NodeConfiguration

class AgentNodeLiveConfigurations(Collection):
    """Used to enumerate a agent node instance's live configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(AgentNodeLiveConfigurations, self).__init__(client, location, 'node-live-configurations',
            AgentNodeLiveConfiguration)


class AgentNodeLiveConfiguration(NodeConfiguration):
    """A live configuration file in a agent node instance

    :ivar str                                                   content:    The configuration's content
    :ivar `vas.gemfire.AgentLiveConfigurations.AgentLiveConfiguration`  group_configuration:    The node configuration's
                                                                                                group configuration
    :ivar `vas.gemfire.AgentNodeInstances.AgentNodeInstance`    instance:   The instance the owns the configuration
    :ivar str                                                   path:       The configuration's path
    :ivar `vas.shared.Security.Security`                        security:   The resource's security
    :var int                                                    size:       The configuration's size
    """

    def __init__(self, client, location):
        super(AgentNodeLiveConfiguration, self).__init__(client, location, 'agent-node-instance', AgentNodeInstance,
            AgentLiveConfiguration)


from vas.gemfire.AgentLiveConfigurations import AgentLiveConfiguration
from vas.gemfire.AgentNodeInstances import AgentNodeInstance
