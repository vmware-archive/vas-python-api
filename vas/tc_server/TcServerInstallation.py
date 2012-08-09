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

class TcServerInstallation(Installation):
    """A tc Server installation

    :ivar `vas.tc_server.TcServerGroup` group: The installation's parent group
    :ivar list instances: The :class:`vas.tc_server.TcServerGroupInstance` s that use this installation
    :ivar `vas.tc_server.TcServerInstallationImage` installation_image: The image the installation is based on
    :ivar list runtime_versions: The runtime versions (:obj:`str`) available in the installation
    :ivar `vas.shared.Security` security:   The security configuration for the type
    :ivar `vas.tc_server.TcServerTemplates` templates: The collection of templates
    :ivar str version: The version of the installation
    """

    __KEY_RUNTIME_VERSIONS = 'runtime-versions'

    __REL_GROUP_INSTANCE = 'group-instance'

    __REL_TEMPLATES = 'templates'

    def __init__(self, client, location):
        super(TcServerInstallation, self).__init__(client, location)

        self.runtime_versions = self._details[self.__KEY_RUNTIME_VERSIONS]
        self.templates = TcServerTemplates(client, self._links[self.__REL_TEMPLATES][0])

    @property
    def instances(self):
        return [TcServerGroupInstance(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_GROUP_INSTANCE)]

    def _create_group(self, client, location):
        return TcServerGroup(client, location)

    def _create_installation_image(self, client, location):
        return TcServerInstallationImage(client, location)

from vas.tc_server.TcServerGroup import TcServerGroup
from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerInstallationImage import TcServerInstallationImage
from vas.tc_server.TcServerTemplates import TcServerTemplates
