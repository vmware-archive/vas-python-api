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
from vas.util.LinkUtils import LinkUtils

class CacheServerInstances(MutableCollection):
    """Used to enumerate, create, and delete cache server instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(CacheServerInstances, self).__init__(client, location, 'cache-server-group-instances',
            CacheServerInstance)

    def create(self, installation, name):
        """Creates a new cache server instance

        :param `vas.gemfire.Installations.Installation` installation:   The installation to be used by the instance
        :param str                                      name:           The name of the instance
        :rtype:     :class:`vas.gemfire.CacheServerInstances.CacheServerInstance`
        :return:    The new cache server instance
        """

        payload = {'installation': installation._location, 'name': name}
        return self._create(payload, 'cache-server-group-instance')


class CacheServerInstance(Instance):
    """A cache server instance

    :ivar `vas.gemfire.Groups.Group`                 group:          The group that contains this instance
    :ivar `vas.gemfire.Installations.Installation`   installation:   The installation that this instance is using
    :ivar `vas.gemfire.LiveApplicationCodes.LiveApplicationCodes`   live_application_code:  The instance's live
                                                                                            application code
    :ivar `vas.gemfire.CacheServerLiveConfigurations.CacheServerLiveConfigurations` live_configurations:    The instance's live
                                                                                                            configurations
    :ivar str                                       name:           The instance's name
    :ivar list                                      node_instances: The instance's individual node instances
    :ivar `vas.gemfire.PendingApplicationCodes.PendingApplicationCodes` pending_application_code:   The instance's
                                                                                                    pending application
                                                                                                    code
    :ivar `vas.gemfire.CacheServerPendingConfigurations.CacheServerPendingConfigurations`   pending_configurations: The instance's
                                                                                                                    pending configurations
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar str                                       state:          Retrieves the state of the resource from the server.
                                                                    Will be one of:

                                                                    * ``STARTING``
                                                                    * ``STARTED``
                                                                    * ``STOPPING``
                                                                    * ``STOPPED``
    """

    __live_application_code = None
    __pending_application_code = None

    @property
    def live_application_code(self):
        self.__live_application_code = self.__live_application_code or LiveApplicationCodes(self._client,
            self.__live_application_code_location)
        return self.__live_application_code

    @property
    def pending_application_code(self):
        self.__pending_application_code = self.__pending_application_code or PendingApplicationCodes(self._client,
            self.__pending_application_code_location)
        return self.__pending_application_code

    def __init__(self, client, location):
        super(CacheServerInstance, self).__init__(client, location, Group, Installation, CacheServerLiveConfigurations,
            CacheServerPendingConfigurations, CacheServerNodeInstance, 'cache-server-node-instance')

        self.__live_application_code_location = LinkUtils.get_link_href(self._details, 'live-application-code')
        self.__pending_application_code_location = LinkUtils.get_link_href(self._details, 'pending-application-code')

    def update(self, installation):
        """Updates the instance to use a different installation

        :param `vas.gemfire.Installations.Installation` installation:   The installation that the instance should use
        """

        self._client.post(self._location, {'installation': installation._location})
        self.reload()


from vas.gemfire.CacheServerLiveConfigurations import CacheServerLiveConfigurations
from vas.gemfire.CacheServerNodeInstances import CacheServerNodeInstance
from vas.gemfire.CacheServerPendingConfigurations import CacheServerPendingConfigurations
from vas.gemfire.Groups import Group
from vas.gemfire.Installations import Installation
from vas.gemfire.LiveApplicationCodes import LiveApplicationCodes
from vas.gemfire.PendingApplicationCodes import PendingApplicationCodes
