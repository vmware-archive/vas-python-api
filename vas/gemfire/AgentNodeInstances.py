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


from vas.shared.NodeInstances import NodeInstances, NodeInstance

class AgentNodeInstances(NodeInstances):
    """Used to enumerate agent instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(AgentNodeInstances, self).__init__(client, location, 'agent-node-instances', AgentNodeInstance)


class AgentNodeInstance(NodeInstance):
    """A agent node instance

    :ivar `vas.gemfire.AgentInstances.AgentInstance`    group_instance: The node instance's group instance
    :ivar `vas.gemfire.AgentLiveConfigurations.AgentLiveConfigurations` live_configurations:    The node instance's live
                                                                                                configuration
    :ivar `vas.gemfire.AgentLogs.AgentLogs`             logs:           The instance's logs
    :ivar str                                           name:           The instance's name
    :ivar `vas.gemfire.Nodes.Nodes`                     node:           The node that contains this instance
    :ivar `vas.shared.Security.Security`                security:       The resource's security
    :ivar str                                           state:          Retrieves the state of the resource from the
                                                                        server. Will be one of:

                                                                        * ``STARTING``
                                                                        * ``STARTED``
                                                                        * ``STOPPING``
                                                                        * ``STOPPED``
    """

    def __init__(self, client, location):
        super(AgentNodeInstance, self).__init__(client, location, Node, AgentLogs, AgentInstance,
            'agent-group-instance', AgentNodeLiveConfigurations)


from vas.gemfire.AgentInstances import AgentInstance
from vas.gemfire.AgentLogs import AgentLogs
from vas.gemfire.AgentNodeLiveConfigurations import AgentNodeLiveConfigurations
from vas.gemfire.Nodes import Node
