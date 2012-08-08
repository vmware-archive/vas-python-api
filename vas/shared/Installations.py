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


from vas.shared.MutableCollectionType import MutableCollectionType

class Installations(MutableCollectionType):
    """An collection of abstract installations

    :ivar `vas.shared.Security` security:   The security configuration for the collection of abstract installations
    """

    __COLLECTION_KEY = 'installations'

    __REL_INSTALLATION = 'installation'

    def __init__(self, client, location):
        super(Installations, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, installation_image):
        """Create a new installation

        :type installation_image:   :class:`vas.shared.InstallationImage`
        :param installation_image:  The installation image to use when creating this installation
        :rtype:     :class:`vas.shared.Installation`
        :return:    The newly created installation
        """
        location = self._client.post(self._location_self, {'image': installation_image._location_self},
            self.__REL_INSTALLATION)
        return self._create_item(self._client, location)
