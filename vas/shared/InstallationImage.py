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
from vas.shared.VersionedImage import VersionedImage
from vas.util.LinkUtils import LinkUtils

class InstallationImage(VersionedImage):
    """An installation image

    :ivar list installations: The :class:`vas.shared.Installation` s that use the installation image
    :ivar `vas.shared.Security` security:   The security configuration for the installation image
    :ivar int size: The size of the image
    :ivar str version: The version of the installation image
    """

    __REL_INSTALLATION = 'installation'

    @property
    def installations(self):
        return [self._create_item(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_INSTALLATION)]

    def _create_item(self, client, location):
        raise VFabricAdministrationServerError('_create_item(self, location) method is unimplemented')
