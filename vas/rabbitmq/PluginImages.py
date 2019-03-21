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

class PluginImages(MutableCollection):
    """Used to enumerate, create, and delete RabbitMQ plugin images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(PluginImages, self).__init__(client, location, 'plugin-images', PluginImage)

    def create(self, path):
        """Creates a new plugin image by uploading a file

        :param str  path:   The path of the plugin ``.ez`` file to upload
        :rtype:     :class:`vas.rabbitmq.PluginImages.PluginImage`
        :return:    The new plugin image
        """

        return self._create_multipart(path)


class PluginImage(Resource, Deletable):
    """A plugin image

    :ivar str                               name:       The plugin image's name
    :ivar `vas.rabbitmq.Plugins.Plugins`    plugins:    The plugins that have been created from this plugin image
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar int                               size:       The plugin image's size
    :ivar str                               version:    The plugin image's version
    """

    @property
    def name(self):
        return self.__name

    @property
    def plugins(self):
        self.__plugins = self.__plugins or self._create_resources_from_links('plugin', Plugin)
        return self.__plugins

    @property
    def size(self):
        return self.__size

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(PluginImage, self).__init__(client, location)

        self.__name = self._details['name']
        self.__size = self._details['size']
        self.__version = self._details['version']

    def reload(self):
        """Reloads the plugin image's details from the server"""

        super(PluginImage, self).reload()
        self.__plugins = None

    def __str__(self):
        return "<{} name={} size={} version={}>".format(self.__class__.__name__, self.__name, self.__size,
            self.__version)


from vas.rabbitmq.Plugins import Plugin
