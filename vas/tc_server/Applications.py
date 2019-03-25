# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Applications(MutableCollection):
    """Used to enumerate, create, and delete applications

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Applications, self).__init__(client, location, 'applications', Application)

    def create(self, name, context_path, service, host):
        """Creates an new application

        :param str  name:           The name of the application
        :param str  context_path:   The context path of the application
        :param str  service:        The service that the application will deploy its revisions to
        :param str  host:           The host that the application will deploy its revisions to
        :rtype:     :class:`vas.tc_server.Applications.Application`
        :return:    The new application
        """

        payload = {
            'context-path': context_path,
            'name': name,
            'host': host,
            'service': service
        }

        return self._create(payload, 'group-application')


class Application(Resource, Deletable):
    """An application

    :ivar str                                   context_path:       The application's context path
    :ivar str                                   host:               The host the application will deploy its revisions
                                                                    to
    :ivar `vas.tc_server.Instances.Instance`    instance:           The instance that contains the application
    :ivar str                                   name:               The application's name
    :ivar list                                  node_applications:  The application's individual node applications
    :ivar `vas.tc_server.Revisions.Revisions`   revisions:          The application's revisions
    :ivar `vas.shared.Security.Security`        security:           The resource's security
    :ivar str                                   service:            The service the application will deploy its
                                                                    revisions to
    """

    __instance = None
    __revisions = None

    @property
    def context_path(self):
        return self.__context_path

    @property
    def host(self):
        return self.__host

    @property
    def instance(self):
        self.__instance = self.__instance or Instance(self._client, self.__instance_location)
        return self.__instance

    @property
    def name(self):
        return self.__name

    @property
    def node_applications(self):
        self.__node_applications = self.__node_applications or self._create_resources_from_links('node-application',
            NodeApplication)
        return self.__node_applications

    @property
    def revisions(self):
        self.__revisions = self.__revisions or Revisions(self._client, self.__revisions_location)
        return self.__revisions

    @property
    def service(self):
        return self.__service

    def __init__(self, client, location):
        super(Application, self).__init__(client, location)

        self.__context_path = self._details['context-path']
        self.__host = self._details['host']
        self.__name = self._details['name']
        self.__service = self._details['service']

        self.__revisions_location = LinkUtils.get_link_href(self._details, 'group-revisions')
        self.__instance_location = LinkUtils.get_link_href(self._details, 'group-instance')

    def reload(self):
        """Reloads the application's details from the server"""

        super(Application, self).reload()
        self.__node_applications = None

    def __str__(self):
        return "<{} name={} context_path={} service={} host={}>".format(self.__class__.__name__, self.__name,
            self.__context_path, self.__service, self.__host)


from vas.tc_server.Instances import Instance
from vas.tc_server.NodeApplications import NodeApplication
from vas.tc_server.Revisions import Revisions
