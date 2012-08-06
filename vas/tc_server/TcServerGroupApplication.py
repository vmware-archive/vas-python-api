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

class TcServerGroupApplication(Type):
    """A tc Server group application

    :ivar str context_path: The context path of the group application
    :ivar `vas.tc_server.TcServerGroupInstance` instance: The group applications' parent group instance
    :ivar `vas.tc_server.TcServerGroupRevisions` revisions:  The collection of group revisions
    :ivar str host: The host of the group application
    :ivar str name: The name of the group application
    :ivar list node_applications: The :class:`vas.tc_server.TcServerNodeApplication` s that are members of the group application
    :ivar `vas.shared.Security` security:   The security configuration for the group application
    :ivar str service: The service of the group application
    """

    __KEY_CONTEXT_PATH = 'context-path'

    __KEY_HOST = 'host'

    __KEY_NAME = 'name'

    __KEY_SERVICE = 'service'

    __REL_GROUP_INSTANCE = 'group-instance'

    __REL_GROUP_REVISIONS = 'group-revisions'

    __REL_NODE_APPLICATION = 'node-application'

    def __init__(self, client, location):
        super(TcServerGroupApplication, self).__init__(client, location)

        self.context_path = self._details[self.__KEY_CONTEXT_PATH]
        self.host = self._details[self.__KEY_HOST]
        self.name = self._details[self.__KEY_NAME]
        self.revisions = TcServerGroupRevisions(client, self._links[self.__REL_GROUP_REVISIONS][0])
        self.service = self._details[self.__KEY_SERVICE]
        self.instance = TcServerGroupInstance(client, self._links[self.__REL_GROUP_INSTANCE][0])

    @property
    def node_applications(self):
        return [TcServerNodeApplication(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_NODE_APPLICATION)]

from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
from vas.tc_server.TcServerGroupRevisions import TcServerGroupRevisions
from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
