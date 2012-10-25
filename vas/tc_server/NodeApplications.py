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


from vas.shared.Collection import Collection
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class NodeApplications(Collection):
    """Used to enumerate a node instance's applications

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(NodeApplications, self).__init__(client, location, 'applications', NodeApplication)


class NodeApplication(Resource):
    """An application on a node instance

    :ivar str                                           context_path:       The application's context path
    :ivar str                                           host:               The host the application will deploy its
                                                                            revisions to
    :ivar `vas.tc_server.Applications.Application`      group_application:  The application that this node application
                                                                            is a member of
    :ivar `vas.tc_server.NodeInstances.NodeInstance`    instance:           The node instance that contains the
                                                                            application
    :ivar str                                           name:               The application's name
    :ivar `vas.tc_server.NodeRevisions.NodeRevisions`   revisions:          The application's revisions
    :ivar `vas.shared.Security.Security`                security:           The resource's security
    :ivar str                                           service:            The service the application will deploy its
                                                                            revisions to
    """

    __group_application = None
    __instance = None
    __revisions = None

    @property
    def context_path(self):
        return self.__context_path

    @property
    def host(self):
        return self.__host

    @property
    def group_application(self):
        self.__group_application = self.__group_application or Application(self._client,
            self.__group_application_location)
        return self.__group_application

    @property
    def instance(self):
        self.__instance = self.__instance or NodeInstance(self._client, self.__instance_location)
        return self.__instance

    @property
    def name(self):
        return self.__name

    @property
    def revisions(self):
        self.__revisions = self.__revisions or NodeRevisions(self._client, self.__revisions_location)
        return self.__revisions

    @property
    def service(self):
        return self.__service

    def __init__(self, client, location):
        super(NodeApplication, self).__init__(client, location)

        self.__context_path = self._details['context-path']
        self.__host = self._details['host']
        self.__name = self._details['name']
        self.__service = self._details['service']

        self.__group_application_location = LinkUtils.get_link_href(self._details, 'group-application')
        self.__instance_location = LinkUtils.get_link_href(self._details, 'node-instance')
        self.__revisions_location = LinkUtils.get_link_href(self._details, 'node-revisions')


from vas.tc_server.Applications import Application
from vas.tc_server.NodeInstances import NodeInstance
from vas.tc_server.NodeRevisions import NodeRevisions
