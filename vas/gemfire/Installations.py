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


import vas.shared.Installations

class Installations(vas.shared.Installations.Installations):
    """Used to enumerate, create, and delete GemFire installations

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Installations, self).__init__(client, location, Installation)


class Installation(vas.shared.Installations.Installation):
    """A GemFire installation

    :ivar list                                                  agent_instances:        The agent instances that are
                                                                                        using the installation
    :ivar list                                                  cache_server_instances: The cache server instances that
                                                                                        are using the installation
    :ivar `vas.gemfire.Groups.Group`                            group:                  The group that contains the
                                                                                        installation
    :ivar `vas.gemfire.InstallationImages.InstallationImage`    installation_image:     The installation image that was
                                                                                        used to create the installation
    :ivar list                                                  locator_instances:      The locator instances that are
                                                                                        using the installation
    :ivar `vas.shared.Security.Security`                        security:               The resource's security
    :ivar str                                                   version:                The installation's version
    """

    @property
    def agent_instances(self):
        self.__agent_instances = self.__agent_instances or self._create_resources_from_links(
            'agent-group-instance', AgentInstance)
        return self.__agent_instances

    @property
    def cache_server_instances(self):
        self.__cache_server_instances = self.__cache_server_instances or self._create_resources_from_links(
            'cache-server-group-instance', CacheServerInstance)
        return self.__cache_server_instances

    @property
    def locator_instances(self):
        self.__locator_instances = self.__locator_instances or self._create_resources_from_links(
            'locator-group-instance', LocatorInstance)
        return self.__locator_instances

    def __init__(self, client, location):
        super(Installation, self).__init__(client, location, InstallationImage, Group)

    def reload(self):
        """Reloads the installation's details from the server"""

        super(Installation, self).reload()

        self.__agent_instances = None
        self.__cache_server_instances = None
        self.__locator_instances = None


from vas.gemfire.AgentInstances import AgentInstance
from vas.gemfire.CacheServerInstances import CacheServerInstance
from vas.gemfire.LocatorInstances import LocatorInstance
from vas.gemfire.Groups import Group
from vas.gemfire.InstallationImages import InstallationImage

