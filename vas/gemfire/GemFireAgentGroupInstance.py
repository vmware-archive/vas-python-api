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


from vas.shared.GroupInstance import GroupInstance

class GemFireAgentGroupInstance(GroupInstance):
    """A GemFire agent group instance


    :ivar `vas.gemfire.GemFireGroup` group: The group instance's parent group
    :ivar `vas.gemfire.GemFireInstallation` installation: The group instance's installation
    :ivar `vas.gemfire.GemFireAgentLiveConfigurations` live_configurations:  The collection of live configurations
    :ivar str name: The name of the group instance
    :ivar list node_instances: The :class:`vas.gemfire.GemFireAgentNodeInstance` s that are members of the group instance
    :ivar `vas.gemfire.GemFireAgentPendingConfigurations` pending_configurations: The collection of pending configurations
    :ivar `vas.shared.Security` security:   The security configuration for group instance
    :ivar str state:    The current state of the group instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __REL_NODE_INSTANCE = 'agent-node-instance'

    def __init__(self, client, location):
        super(GemFireAgentGroupInstance, self).__init__(client, location, self.__REL_NODE_INSTANCE)

    def update(self, installation):
        """Update the agent group instance to use a different installation

        :type installation:    :class:`vas.gemfire.GemFireInstallation`
        :param installation:   The installation to use when running the instance
        """

        self._client.post(self._location_self, {'installation': installation._location_self})

    def _create_group(self, client, location):
        return GemFireGroup(client, location)

    def _create_installation(self, client, location):
        return GemFireInstallation(client, location)

    def _create_live_configurations(self, client, location):
        return GemFireAgentLiveConfigurations(client, location)

    def _create_node_instance(self, client, location):
        return GemFireAgentNodeInstance(client, location)

    def _create_pending_configurations(self, client, location):
        return GemFireAgentPendingConfigurations(client, location)

from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireInstallation import GemFireInstallation
from vas.gemfire.GemFireAgentLiveConfigurations import GemFireAgentLiveConfigurations
from vas.gemfire.GemFireAgentNodeInstance import GemFireAgentNodeInstance
from vas.gemfire.GemFireAgentPendingConfigurations import GemFireAgentPendingConfigurations
