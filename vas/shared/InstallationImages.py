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


class InstallationImages(MutableCollection):
    """A collection of installation images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location, installation_image_class):
        super(InstallationImages, self).__init__(client, location, 'installation-images', installation_image_class)

    def create(self, path, version):
        """Creates an installation image by uploading a file to the server and assigning it a version

        :param str  path:       The path of the file to upload
        :param str  version:    The installation image's version
        :rtype:     :class:`vas.shared.InstallationImages.InstallationImage`
        :return:    The new installation image
        """

        return self._create_multipart(path, {'version': version})


class InstallationImage(Resource, Deletable):
    """A product binary, typically are .zip or .tar.gz file, that has been uploaded to the server. Once created, an
    installation image can then be used to create an installation on a group.

    :ivar `vas.shared.Installations.Installations`  installations:  The installations that have been created from the
                                                                    installation image
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar int                                       size:           The installation image's size
    :ivar str                                       version:        The installation image's version
    """

    @property
    def installations(self):
        self.__installations = self.__installations or self._create_resources_from_links('installation',
            self.__installation_class)
        return self.__installations

    @property
    def size(self):
        return self.__size

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location, installation_class):
        super(InstallationImage, self).__init__(client, location)

        self.__installation_class = installation_class

        self.__size = self._details['size']
        self.__version = self._details['version']

    def reload(self):
        """Reloads the installation image's details from the server"""

        super(InstallationImage, self).reload()
        self.__installations = None

    def __str__(self):
        return "<{} version={} size={}>".format(self.__class__.__name__, self.__version, self.__size)
