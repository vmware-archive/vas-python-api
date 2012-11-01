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
    """An agent node instance

    :ivar `vas.sqlfire.AgentInstances.AgentInstance`    group_instance:         The node instance's group instance
    :ivar list                                          jvm_options:            The JVM options that are passed to the
                                                                                agent's JVM when it is started
    :ivar `vas.sqlfire.AgentNodeLiveConfigurations.AgentNodeLiveConfigurations` live_configurations:    The node instance's
                                                                                                        live configuration
    :ivar `vas.sqlfire.AgentLogs.AgentLogs`             logs:                   The instance's logs
    :ivar str                                           name:                   The instance's name
    :ivar `vas.sqlfire.Nodes.Nodes`                      node:                   The node that contains this instance
    :ivar `vas.shared.Security.Security`                security:               The resource's security
    :ivar str                                           state:                  Retrieves the state of the resource from the
                                                                                server. Will be one of:

                                                                                * ``STARTING``
                                                                                * ``STARTED``
                                                                                * ``STOPPING``
                                                                                * ``STOPPED``
    """

    @property
    def jvm_options(self):
        return self.__jvm_options

    def __init__(self, client, location):
        super(AgentNodeInstance, self).__init__(client, location, Node, AgentLogs, AgentInstance,
            'agent-group-instance', AgentNodeLiveConfigurations)

    def reload(self):
        """Reloads the agent instance's details from the server"""

        super(AgentNodeInstance, self).reload()

        self.__jvm_options = self._details['jvm-options']

    def __str__(self):
        return "<{} name={} jvm_options={}>".format(self.__class__, self.name, self.__jvm_options)


from vas.sqlfire.AgentInstances import AgentInstance
from vas.sqlfire.AgentLogs import AgentLogs
from vas.sqlfire.AgentNodeLiveConfigurations import AgentNodeLiveConfigurations
from vas.sqlfire.Nodes import Node
