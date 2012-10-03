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


from vas.shared.NamedImage import NamedImage
from vas.util.LinkUtils import LinkUtils

class GemFireApplicationCodeImage(NamedImage):
    """An application code image

    :ivar str name: The name of the application code image
    :ivar `vas.shared.Security` security:   The security configuration for the application code image
    :ivar list live_application_code: The :class:`vas.gemfire.GemFireLiveApplicationCode` s that use the application code image
    :ivar list pending_application_code: The :class:`vas.gemfire.GemFirePendingApplicationCode` s that use the application code image
    :ivar int size: The size of the application code image
    :ivar str version: The version of the application image
    """

    __REL_LIVE_APPLICATION_CODE = 'live-application-code'

    __REL_PENDING_APPLICATION_CODE = 'pending-application-code'

    @property
    def live_application_code(self):
        return [GemFireLiveApplicationCode(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_LIVE_APPLICATION_CODE)]

    @property
    def pending_application_code(self):
        return [GemFirePendingApplicationCode(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_PENDING_APPLICATION_CODE)]


from vas.gemfire.GemFireLiveApplicationCode import GemFireLiveApplicationCode
from vas.gemfire.GemFirePendingApplicationCode import GemFirePendingApplicationCode
