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


from vas.shared.Installation import Installation
from vas.util.LinkUtils import LinkUtils

class GemFireInstallation(Installation):
    """A GemFire installation

    :ivar `vas.gemfire.GemFireGroup` group: The installation's parent group
    :ivar list agent_instances: The :class:`vas.gemfire.GemFireAgentGroupInstance` s that use this installation
    :ivar list cache_server_instances: The :class:`vas.gemfire.GemFireCacheServerGroupInstance` s that use this installation
    :ivar `vas.gemfire.GemFireInstallationImage` installation_image: The image the installation is based on
    :ivar list locator_instances: The :class:`vas.gemfire.GemFireLocatorGroupInstance` s that use this installation
    :ivar `vas.shared.Security` security:   The security configuration for the type
    :ivar str version: The version of the installation
    """

    __REL_AGENT_GROUP_INSTANCE = 'agent-group-instance'

    __REL_CACHE_SERVER_GROUP_INSTANCE = 'cache-server-group-instance'

    __REL_LOCATOR_GROUP_INSTANCE = 'locator-group-instance'

    @property
    def agent_instances(self):
        return [GemFireAgentGroupInstance(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_AGENT_GROUP_INSTANCE)]

    @property
    def cache_server_instances(self):
        return [GemFireCacheServerGroupInstance(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_CACHE_SERVER_GROUP_INSTANCE)]

    @property
    def locator_instances(self):
        return [GemFireLocatorGroupInstance(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_LOCATOR_GROUP_INSTANCE)]

    def _create_group(self, client, location):
        return GemFireGroup(client, location)

    def _create_installation_image(self, client, location):
        return GemFireInstallationImage(client, location)

from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireAgentGroupInstance import GemFireAgentGroupInstance
from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFireInstallationImage import GemFireInstallationImage
from vas.gemfire.GemFireLocatorGroupInstance import GemFireLocatorGroupInstance
