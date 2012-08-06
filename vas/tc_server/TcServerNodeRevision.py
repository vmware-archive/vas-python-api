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

class TcServerNodeRevision(Type):
    """A tc Server node revision

    :ivar `vas.tc_server.TcServerGroupRevision` group_revision: The group revision that the node revision is a member of
    :ivar `vas.tc_server.TcServerNodeApplication` application: The node revision's parent node application
    :ivar str state:    The current state of the group revision.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    :ivar `vas.shared.Security` security:   The security configuration for the group revision
    :ivar str version: The version of the group revision
    """

    __KEY_VERSION = 'version'

    __REL_GROUP_REVISION = 'group-revision'

    __REL_NODE_APPLICATION = 'node-application'

    __REL_STATE = 'state'

    def __init__(self, client, location):
        super(TcServerNodeRevision, self).__init__(client, location)

        self.version = self._details[self.__KEY_VERSION]
        self.group_revision = TcServerGroupRevision(client, self._links[self.__REL_GROUP_REVISION][0])
        self.application = TcServerNodeApplication(client, self._links[self.__REL_NODE_APPLICATION][0])
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

from vas.tc_server.TcServerGroupRevision import TcServerGroupRevision
from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
