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

class GemFirePendingApplicationCodes(MutableCollectionType):
    """An collection of pending application codes

    :ivar `vas.shared.Security` security:   The security configuration for the collection of pending application codes
    """

    __COLLECTION_KEY = 'pending-application-code'

    def __init__(self, client, location):
        super(GemFirePendingApplicationCodes, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, application_code_image):
        """Create a new template

        :type application_code_image:   :class:`vas.gemfire.GemFireApplicationCodeImage`
        :param application_code_image:  The application code image to use when creating this application code
        :rtype:         :class:`vas.gemfire.GemFirePendingApplicationCode`
        :return:        The newly created pending application code
        """

        location = self._client.post(self._location_self, {'image': application_code_image._location_self})
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return GemFirePendingApplicationCode(client, location)

from GemFirePendingApplicationCode import GemFirePendingApplicationCode
