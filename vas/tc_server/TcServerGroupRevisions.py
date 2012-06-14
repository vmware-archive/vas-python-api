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

class TcServerGroupRevisions(MutableCollectionType):
    """A collection of tc Server group revisions

    :ivar `vas.shared.Security` security:   The security configuration for the collection of group revisions
    """

    __COLLECTION_KEY = 'revisions'

    __REL_GROUP_REVISION = 'group-revision'

    def __init__(self, client, location):
        super(TcServerGroupRevisions, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, revision_image):
        """Create a new revision

        :type revision_image:   :class:`vas.tc_server.TcServerRevisionImage`
        :param revision_image:  The revision image to use when creating this group revision
        :rtype:         :class:`vas.tc_server.TcServerGroupRevision`
        :return:        The newly created group revision
        """

        location = self._client.post(self._location_self, {'image': revision_image._location_self},
            self.__REL_GROUP_REVISION)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return TcServerGroupRevision(client, location)

from vas.tc_server.TcServerGroupRevision import TcServerGroupRevision
