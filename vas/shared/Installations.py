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
from vas.util.LinkUtils import LinkUtils

class Installations(MutableCollection):
    """A collection of installations

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location, installation_class):
        super(Installations, self).__init__(client, location, 'installations', installation_class)

    def create(self, installation_image):
        """Create a new installation

        :type   installation_image: :class:`vas.shared.InstallationImages.InstallationImage`
        :param  installation_image: The installation image to use to create the installation
        :rtype:     :class:`vas.shared.Installations.Installation`
        :return:    The new installation
        """

        return self._create({'image': installation_image._location}, 'installation')


class Installation(Resource, Deletable):
    """An installation of a middleware component. Created from an installation image. Once created, an installation is
    used when creating a new instance and provides the binaries that the instance uses at runtime.

    :ivar `vas.shared.Groups.Group`                         group:              The group that contains the installation
    :ivar `vas.shared.InstallationImages.InstallationImage` installation_image: The installation image that was used to
                                                                                create the installation
    :ivar `vas.shared.Security.Security`                    security:           The resource's security
    :ivar str                                               version:            The installation's version
    """

    __group = None
    __installation_image = None

    @property
    def group(self):
        self.__group = self.__group or self.__group_class(self._client, self.__group_location)
        return self.__group

    @property
    def installation_image(self):
        self.__installation_image = self.__installation_image or self.__installation_image_class(self._client,
            self.__installation_image_location)
        return self.__installation_image

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location, installation_image_class, group_class):
        super(Installation, self).__init__(client, location)

        self.__installation_image_location = LinkUtils.get_link_href(self._details, 'installation-image')
        self.__group_location = LinkUtils.get_link_href(self._details, 'group')

        self.__installation_image_class = installation_image_class
        self.__group_class = group_class

        self.__version = self._details['version']

    def __str__(self):
        return "<{} version={}>".format(self.__class__.__name__, self.__version)

