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

    def create(self, installation, name, jvm_options=None):
        """Creates a new agent instance

        :param `vas.sqlfire.Installations.Installation` installation:   The installation ot be used by the instance
        :param str                                      name:           The name of the instances
        :param list                                     jvm_options:    The JVM options that are based to the agent's
                                                                        JVM when it is started
        :rtype:     :class:`vas.sqlfire.AgentInstances.AgentInstance`
        :return:    The new agent instance
        """
        payload = {'installation': installation._location, 'name': name}

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        return self._create(payload, 'agent-group-instance')


class AgentInstance(Instance):
    """An agent instance

    :ivar `vas.sqlfire.Groups.Group`                group:          The group that contains this instance
    :ivar `vas.sqlfire.Installations.Installation`  installation:   The installation that this instance is using
    :ivar list                                      jvm_options:    The JVM options that are passed to the agent's JVM
                                                                    when it is started
    :ivar `vas.sqlfire.AgentLiveConfigurations.AgentLiveConfigurations` live_configurations:    The instance's live
                                                                                                configurations
    :ivar str                                       name:           The instance's name
    :ivar list                                      node_instances: The instance's individual node instances
    :ivar `vas.sqlfire.AgentPendingConfigurations.AgentPendingConfigurations`   pending_configurations: The instance's pending
                                                                                                        configurations
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar str                                       state:          Retrieves the state of the resource from the server.
                                                                    Will be one of:

                                                                    * ``STARTING``
                                                                    * ``STARTED``
                                                                    * ``STOPPING``
                                                                    * ``STOPPED``
    """

    @property
    def jvm_options(self):
        return self.__jvm_options

    def __init__(self, client, location):
        super(AgentInstance, self).__init__(client, location, Group, Installation, AgentLiveConfigurations,
            AgentPendingConfigurations, AgentNodeInstance, 'agent-node-instance')

    def reload(self):
        """Reloads the agent instance's details from the server"""

        super(AgentInstance, self).reload()

        self.__jvm_options = self._details['jvm-options']

    def update(self, installation=None, jvm_options=None):
        """Updates the instance

        :param `vas.sqlfire.Installations.Installation` installation:   The installation to be used by the instance. If
                                                                        omitted or `None`, the configuration will not be
                                                                        changed
        :param list                                     jvm_options:    The JVM options that are passed to the agent's
                                                                        JVM when it is started. If omitted or `None`,
                                                                        the configuration will not be changed
        """

        payload = {}

        if installation:
            payload['installation'] = installation._location

        if jvm_options is not None:
            payload['jvm-options'] = jvm_options

        self._client.post(self._location, payload)
        self.reload()

    def __str__(self):
        return "<{} name={} jvm_options={}>".format(self.__class__, self.name, self.__jvm_options)

from vas.sqlfire.AgentLiveConfigurations import AgentLiveConfigurations
from vas.sqlfire.AgentNodeInstances import AgentNodeInstance
from vas.sqlfire.AgentPendingConfigurations import AgentPendingConfigurations
from vas.sqlfire.Groups import Group
from vas.sqlfire.Installations import Installation
