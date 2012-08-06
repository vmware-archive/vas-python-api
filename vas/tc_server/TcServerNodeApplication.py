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

class TcServerNodeApplication(Type):
    """A tc Server node application

    :ivar str context_path: The context path of the node application
    :ivar `vas.tc_server.TcServerGroupApplication` group_application: The group application that the node application is a member of
    :ivar str host: The host of the node application
    :ivar str name: The name of the node  application
    :ivar `vas.tc_server.TcServerNodeInstance` instance: The The node application's parent node instance
    :ivar `vas.tc_server.TcServerNodeRevisions` revisions:  The collection of node revisions
    :ivar `vas.shared.Security` security:   The security configuration for the node application
    :ivar str service: The service of the node application
    """

    __KEY_CONTEXT_PATH = 'context-path'

    __KEY_HOST = 'host'

    __KEY_NAME = 'name'

    __KEY_SERVICE = 'service'

    __REL_GROUP_APPLICATION = 'group-application'

    __REL_NODE_INSTANCE = 'node-instance'

    __REL_NODE_REVISIONS = 'node-revisions'

    def __init__(self, client, location):
        super(TcServerNodeApplication, self).__init__(client, location)

        self.context_path = self._details[self.__KEY_CONTEXT_PATH]
        self.group_application = TcServerGroupApplication(client, self._links[self.__REL_GROUP_APPLICATION][0])
        self.host = self._details[self.__KEY_HOST]
        self.instance = TcServerNodeInstance(client, self._links[self.__REL_NODE_INSTANCE][0])
        self.name = self._details[self.__KEY_NAME]
        self.revisions = TcServerNodeRevisions(client, self._links[self.__REL_NODE_REVISIONS][0])
        self.service = self._details[self.__KEY_SERVICE]

from vas.tc_server.TcServerNodeInstance import TcServerNodeInstance
from vas.tc_server.TcServerNodeRevisions import TcServerNodeRevisions
from vas.tc_server.TcServerGroupApplication import TcServerGroupApplication
