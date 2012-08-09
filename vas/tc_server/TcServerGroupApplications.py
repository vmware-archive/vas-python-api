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

class TcServerGroupApplications(MutableCollectionType):
    """A collection of tc Server group applications

    :ivar `vas.shared.Security` security:   The security configuration for the collection of group applications
    """

    __COLLECTION_KEY = 'applications'

    __REL_GROUP_APPLICATION = 'group-application'

    def __init__(self, client, location):
        super(TcServerGroupApplications, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, context_path, host, name, service):
        """Create a new group application

        :type context_path:     :obj:`str`
        :param context_path:    The context path of the group application
        :type host:     :obj:`str`
        :param host:    The host the group application should be deployed in
        :type name:     :obj:`str`
        :param name:    The name of the group application
        :type service:  :obj:`str`
        :param service: The service the group application should be deployed in
        :rtype:         :class:`vas.tc_server.TcServerGroupApplication`
        :return:        The newly created group application
        """

        location = self._client.post(self._location_self,
            {'context-path': context_path, 'host': host, 'name': name, 'service': service},
            self.__REL_GROUP_APPLICATION)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return TcServerGroupApplication(client, location)

from vas.tc_server.TcServerGroupApplication import TcServerGroupApplication
