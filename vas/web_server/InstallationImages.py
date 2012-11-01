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


import vas.shared.InstallationImages

class InstallationImages(vas.shared.InstallationImages.InstallationImages):
    """Used to enumerate, create, and delete Web Server installation images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(InstallationImages, self).__init__(client, location, InstallationImage)

    #noinspection PyMethodOverriding
    def create(self, path, version, architecture, operating_system):
        """Creates an installation image by uploading a file to the server and assigning it a version, architecture, and
         operating system

        :param str  path:               The path of the file to upload
        :param str  version:            The installation image's version
        :param str  architecture:       The installation image's architecture
        :param str  operating_system:   The installation image's operating system
        :rtype:     :class:`vas.web_server.InstallationImages.InstallationImage`
        :return:    The new installation image
        """

        payload = {'version': version, 'architecture': architecture, 'operating-system': operating_system}
        return self._create_multipart(path, payload)


class InstallationImage(vas.shared.InstallationImages.InstallationImage):
    """A Web Server installation image

    :ivar str                                           architecture:       The installation image's architecture
    :ivar `vas.web_server.Installations.Installations`  installations:      The installations that have been created
                                                                            from the installation image
    :ivar str                                           operating_system:   The installation image's operating system
    :ivar `vas.shared.Security.Security`                security:           The resource's security
    :ivar int                                           size:               The installation image's size
    :ivar str                                           version:            The installation image's version
    """

    @property
    def architecture(self):
        return self.__architecture

    @property
    def operating_system(self):
        return self.__operating_system

    def __init__(self, client, location):
        super(InstallationImage, self).__init__(client, location, Installation)

        self.__architecture = self._details['architecture']
        self.__operating_system = self._details['operating-system']


from vas.web_server.Installations import Installation
