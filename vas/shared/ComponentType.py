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
from vas.shared.TopLevelType import TopLevelType

class ComponentType(TopLevelType):
    """An abstract component of the vFabric Administration Server

    :ivar `vas.shared.Groups` groups:  The collection of groups
    :ivar `vas.shared.InstallationImages` installation_images:  The collection of installation images
    """

    __REL_GROUPS = 'groups'

    __REL_INSTALLATION_IMAGES = 'installation-images'

    def __init__(self, client, location):
        super(ComponentType, self).__init__(client, location)

        self.groups = self._create_groups(client, self._links[self.__REL_GROUPS][0])
        self.installation_images = self._create_installation_images(client,
            self._links[self.__REL_INSTALLATION_IMAGES][0])

    def _create_groups(self, client, location):
        raise VFabricAdministrationServerError('_create_groups(self, client, location) method is unimplemented')

    def _create_installation_images(self, client, location):
        raise VFabricAdministrationServerError(
            '_create_installation_images(self, client, location) method is unimplemented')
