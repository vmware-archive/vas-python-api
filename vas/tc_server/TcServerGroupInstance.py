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

class TcServerGroupInstance(GroupInstance):
    """A tc Server group instance


    :ivar `vas.tc_server.TcServerGroup` group: The group instance's parent group
    :ivar `vas.tc_server.TcServerGroupApplications` applications: The collection of group applications
    :ivar `vas.tc_server.TcServerInstallation` installation: The group instance's installation
    :ivar str layout:   The layout of the group instance
    :ivar `vas.tc_server.TcServerLiveConfigurations` live_configurations:  The collection of live configurations
    :ivar str name: The name of the group instance
    :ivar list node_instances: The :class:`vas.tc_server.TcServerNodeInstance` s that are members of the group instance
    :ivar `vas.tc_server.TcServerPendingConfigurations` pending_configurations: The collection of pending configurations
    :ivar str runtime_version:  The runtime version of the group instance
    :ivar `vas.shared.Security` security:   The security configuration for group instance
    :ivar str services: The services configured in the group instance
    :ivar str state:    The current state of the group instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """
    __KEY_LAYOUT = 'layout'

    __KEY_RUNTIME_VERSION = 'runtime-version'

    __KEY_SERVICES = 'services'

    __REL_GROUP_APPLICATIONS = 'group-applications'

    __REL_NODE_INSTANCE = 'node-instance'

    def __init__(self, client, location):
        super(TcServerGroupInstance, self).__init__(client, location, self.__REL_NODE_INSTANCE)

        self.applications = TcServerGroupApplications(client, self._links[self.__REL_GROUP_APPLICATIONS][0])
        self.layout = self._details[self.__KEY_LAYOUT]
        self.runtime_version = self._details[self.__KEY_RUNTIME_VERSION]
        self.services = self._details[self.__KEY_SERVICES]


    def update(self, installation, runtime_version=None):
        """Update the group instance to use a different installation, optionally specifying a new runtime version to be used with the new installation

        :type installation:    :class:`vas.tc_server.TcServerInstallation`
        :param installation:   The installation to use when running the instance
        :type runtime_version:  :obj:`str`
        :param runtime_version: The runtime version to use when running the instance
        """

        payload = dict()
        payload['installation'] = installation._location_self

        if runtime_version is not None:
            payload['runtime-version'] = runtime_version

        self._client.post(self._location_self, payload)

    def _create_group(self, client, location):
        return TcServerGroup(client, location)

    def _create_installation(self, client, location):
        return TcServerInstallation(client, location)

    def _create_live_configurations(self, client, location):
        return TcServerLiveConfigurations(client, location)

    def _create_node_instance(self, client, location):
        return TcServerNodeInstance(client, location)

    def _create_pending_configurations(self, client, location):
        return TcServerPendingConfigurations(client, location)

from vas.tc_server.TcServerGroup import TcServerGroup
from vas.tc_server.TcServerGroupApplications import TcServerGroupApplications
from vas.tc_server.TcServerInstallation import TcServerInstallation
from vas.tc_server.TcServerLiveConfigurations import TcServerLiveConfigurations
from vas.tc_server.TcServerNodeInstance import TcServerNodeInstance
from vas.tc_server.TcServerPendingConfigurations import TcServerPendingConfigurations
