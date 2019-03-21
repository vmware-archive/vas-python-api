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


from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Configuration(Resource):
    """A configuration file in an instance

    :ivar str                               content:    The configuration's content
    :ivar `vas.shared.Instance.Instance`    instance:   The instance the owns the configuration
    :ivar str                               path:       The configuration's path
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar int                               size:       The configuration's size
    """

    __instance = None

    @property
    def content(self):
        return self._client.get(self.__content_location)

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

    @property
    def _content_location(self):
        return self.__content_location


    def __init__(self, client, location, instance_type, instance_class):
        super(Configuration, self).__init__(client, location)

        self.__instance_class = instance_class

        self.__instance_location = LinkUtils.get_link_href(self._details, instance_type)
        self.__content_location = LinkUtils.get_link_href(self._details, 'content')

        self.__path = self._details['path']

    def reload(self):
        """Reloads the configuration's details from the server"""

        super(Configuration, self).reload()
        self.__size = self._details['size']

    def __str__(self):
        return "<{} path={} size={}>".format(self.__class__.__name__, self.__path, self.__size)

