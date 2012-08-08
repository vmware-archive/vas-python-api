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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.Type import Type

class Installation(Type):
    """An abstract installation

    :ivar `vas.shared.Group` group: The installation's parent group
    :ivar `vas.shared.InstallationImage` installation_image: The image the installation is based on
    :ivar `vas.shared.Security` security:   The security configuration for the installation
    :ivar str version: The version of the installation
    """

    __KEY_VERSION = 'version'

    __REL_GROUP = 'group'

    __REL_INSTALLATION_IMAGE = 'installation-image'

    def __init__(self, client, location):
        super(Installation, self).__init__(client, location)

        self.group = self._create_group(client, self._links[self.__REL_GROUP][0])
        self.installation_image = self._create_installation_image(client, self._links[self.__REL_INSTALLATION_IMAGE][0])
        self.version = self._details[self.__KEY_VERSION]


    def _create_group(self, client, location):
        raise VFabricAdministrationServerError('_create_group(self, client, location) method is unimplemented')

    def _create_installation_image(self, client, location):
        raise VFabricAdministrationServerError(
            '_create_installation_image(self, client, location) method is unimplemented')
