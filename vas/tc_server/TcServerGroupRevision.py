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


from vas.shared.Type import Type
from vas.util.LinkUtils import LinkUtils

class TcServerGroupRevision(Type):
    """A tc Server group revision

    :ivar `vas.tc_server.TcServerGroupApplication` application: The group revision's parent group application
    :ivar list node_revisions: The :class:`vas.tc_server.TcServerNodeRevision` s that are members of the group revision
    :ivar `vas.tc_server.TcServerRevisionImage` revision_image: The image the group revision is based on
    :ivar `vas.shared.Security` security:   The security configuration for the group revision
    :ivar str state:    The current state of the group revision.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    :ivar str version: The version of the group revision
    """

    __KEY_VERSION = 'version'

    __REL_GROUP_APPLICATION = 'group-application'

    __REL_NODE_REVISION = 'node-revision'

    __REL_REVISION_IMAGE = 'revision-image'

    __REL_STATE = 'state'

    def __init__(self, client, location):
        super(TcServerGroupRevision, self).__init__(client, location)

        self.application = TcServerGroupApplication(client, self._links[self.__REL_GROUP_APPLICATION][0])
        self.revision_image = TcServerRevisionImage(client, self._links[self.__REL_REVISION_IMAGE][0])
        self.version = self._details[self.__KEY_VERSION]
        self.__location_state = self._links[self.__REL_STATE][0]

    def start(self):
        """Start the group revision by attempting to set its ``status`` to ``STARTED``"""

        self._client.post(self.__location_state, {'status': 'STARTED'})

    def stop(self):
        """Stop the group revision by attempting to set its ``status`` to ``STOPPED``"""

        self._client.post(self.__location_state, {'status': 'STOPPED'})

    @property
    def state(self):
        return self._client.get(self.__location_state)['status']

    @property
    def node_revisions(self):
        return [TcServerNodeRevision(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_NODE_REVISION)]

from vas.tc_server.TcServerNodeRevision import TcServerNodeRevision
from vas.tc_server.TcServerRevisionImage import TcServerRevisionImage
from vas.tc_server.TcServerGroupApplication import TcServerGroupApplication
