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


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource

class TemplateImages(MutableCollection):
    """ Used to enumerate, create, and delete tc Server template images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(TemplateImages, self).__init__(client, location, 'template-images', TemplateImage)

    def create(self, path, name, version):
        """Creates a new template image by uploading a ``.zip`` file to the server

        :param str  path:       The path of the template image ``.zip`` file
        :param str  name:       The name of the template image
        :param str  version:    The version of the template image
        :rtype:     :class:`vas.tc_server.TemplateImages.TemplateImage`
        :return:    The new template image
        """

        return self._create_multipart(path, {'name': name, 'version': version})


class TemplateImage(Resource, Deletable):
    """A template image

    :ivar str                               name:       The template image's name
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar int                               size:       The template image's size
    :ivar list                              templates:  The templates that have been created from the template image
    :ivar str                               version:    The template image's version
    """

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def templates(self):
        self.__templates = self.__templates or self._create_resources_from_links('template', Template)
        return self.__templates

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(TemplateImage, self).__init__(client, location)

        self.__name = self._details['name']
        self.__size = self._details['size']
        self.__version = self._details['version']

    def reload(self):
        """Reloads the template image's details from the server"""

        super(TemplateImage, self).reload()
        self.__templates = None


from vas.tc_server.Templates import Template
