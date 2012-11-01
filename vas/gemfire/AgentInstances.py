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


from vas.shared.Instance import Instance
from vas.shared.MutableCollection import MutableCollection

class AgentInstances(MutableCollection):
    """Used to enumerate, create, and delete agent instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(AgentInstances, self).__init__(client, location, 'agent-group-instances', AgentInstance)


    def create(self, installation, name):
        """Creates a new agent instance

        :param `vas.gemfire.Installations.Installation` installation:   The installation to be used by the instance
        :param str                                      name:           The name of the instance
        :rtype:     :class`vas.gemfire.AgentInstances.AgentInstance`
        :return:    The new agent instance
        """

        payload = {'installation': installation._location, 'name': name}
        return self._create(payload, 'agent-group-instance')


class AgentInstance(Instance):
    """An agent instance

    :ivar `vas.gemfire.Groups.Group`                group:          The group that contains this instance
    :ivar `vas.gemfire.Installations.Installation`  installation:   The installation that this instance is using
    :ivar `vas.gemfire.AgentLiveConfigurations.AgentLiveConfigurations` live_configurations:    The instance's live configurations
    :ivar str                                       name:           The instance's name
    :ivar list                                      node_instances: The instance's individual node instances
    :ivar `vas.gemfire.AgentPendingConfigurations.AgentPendingConfigurations`   pending_configurations: The instance's
                                                                                                        pending configurations
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar str                                       state:          Retrieves the state of the resource from the server.
                                                                    Will be one of:

                                                                    * ``STARTING``
                                                                    * ``STARTED``
                                                                    * ``STOPPING``
                                                                    * ``STOPPED``
    """

    def __init__(self, client, location):
        super(AgentInstance, self).__init__(client, location, Group, Installation, AgentLiveConfigurations,
            AgentPendingConfigurations, AgentNodeInstance, 'agent-node-instance')

    def update(self, installation):
        """Update he instance to use a different installation

        :param `vas.gemfire.Installations.Installation`  installation:   The installation that the instance should use
        """

        self._client.post(self._location, {'installation': installation._location})
        self.reload()


from vas.gemfire.AgentLiveConfigurations import AgentLiveConfigurations
from vas.gemfire.AgentNodeInstances import AgentNodeInstance
from vas.gemfire.AgentPendingConfigurations import AgentPendingConfigurations
from vas.gemfire.Groups import Group
from vas.gemfire.Installations import Installation
