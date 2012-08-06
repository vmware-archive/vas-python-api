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

class TcServerRevisionImage(NamedImage):
    """A revision image

    :ivar str name: The name of the revision image
    :ivar list revisions: The :class:`vas.tc_server.TcServerGroupRevision` s that use the revision image
    :ivar `vas.shared.Security` security:   The security configuration for the revision image
    :ivar int size: The size of the revision image
    :ivar str version: The version of the revision image
    """

    __REL_REVISION = 'group-revision'

    @property
    def revisions(self):
        return [TcServerGroupRevision(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_REVISION)]


from vas.tc_server.TcServerGroupRevision import TcServerGroupRevision
