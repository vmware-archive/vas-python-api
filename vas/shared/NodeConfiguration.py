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


from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class NodeConfiguration(Resource):
    """A configuration file in a node instance

    :ivar str                                       content:                The configuration's content
    :ivar `vas.shared.Configuration.Configuration`  group_configuration:    The node configuration's group configuration
    :ivar `vas.shared.NodeInstances.NodeInstance`   instance:               The instance the owns the configuration
    :ivar str                                       path:                   The configuration's path
    :ivar `vas.shared.Security.Security`            security:               The resource's security
    :var int                                        size:                   The configuration's size
    """

    __group_configuration = None
    __instance = None

    @property
    def content(self):
        return self._client.get(self.__content_location)

    @property
    def group_configuration(self):
        self.__group_configuration = self.__group_configuration or self.__group_configuration_class(self._client,
            self.__group_configuration_location)
        return self.__group_configuration

    @property
    def instance(self):
        self.__instance = self.__instance or self.__instance_class(self._client, self.__instance_location)
        return self.__instance

    @property
    def path(self):
        return self.__path

    @property
    def size(self):
        return self.__size


    def __init__(self, client, location, instance_type, instance_class, group_configuration_class):
        super(NodeConfiguration, self).__init__(client, location)

        self.__instance_class = instance_class
        self.__group_configuration_class = group_configuration_class

        self.__instance_location = LinkUtils.get_link_href(self._details, instance_type)
        self.__group_configuration_location = LinkUtils.get_link_href(self._details, 'group-live-configuration')
        self.__content_location = LinkUtils.get_link_href(self._details, 'content')

        self.__path = self._details['path']

    def reload(self):
        """Reloads the configuration's details from the server"""

        super(NodeConfiguration, self).reload()
        self.__size = self._details['size']
