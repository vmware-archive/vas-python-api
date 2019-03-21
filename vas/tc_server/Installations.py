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


import vas.shared.Installations
from vas.util.LinkUtils import LinkUtils

class Installations(vas.shared.Installations.Installations):
    """Used to enumerate, create, and delete tc Server installations

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Installations, self).__init__(client, location, Installation)


class Installation(vas.shared.Installations.Installation):
    """A tc Server installation

    :ivar `vas.tc_server.Groups.Group`                          group:              The group that contains the
                                                                                    installation
    :ivar `vas.tc_server.InstallationImages.InstallationImage`  installation_image: The installation image that was used
                                                                                    to create the installation
    :ivar list                                                  instances:          The instances that are using the
                                                                                    installation
    :ivar list                                                  runtime_versions:   The versions of the tc Server
                                                                                    runtime that are supported by the
                                                                                    installation
    :ivar `vas.shared.Security.Security`                        security:           The resource's security
    :ivar `vas.tc_server.Templates.Templates`                   templates:          The installation's templates
    :ivar str                                                   version:            The installation's version
    """

    __templates = None

    @property
    def instances(self):
        self.__instances = self.__instances or self._create_resources_from_links('group-instance', Instance)
        return self.__instances

    @property
    def runtime_versions(self):
        return self.__runtime_versions

    @property
    def templates(self):
        self.__templates = self.__templates or Templates(self._client, self.__templates_location)
        return self.__templates

    def __init__(self, client, location):
        super(Installation, self).__init__(client, location, InstallationImage, Group)

        self.__runtime_versions = self._details['runtime-versions']

        self.__templates_location = LinkUtils.get_link_href(self._details, 'templates')

    def reload(self):
        """Reloads the installation's details from the server"""

        super(Installation, self).reload()
        self.__instances = None


from vas.tc_server.Groups import Group
from vas.tc_server.InstallationImages import InstallationImage
from vas.tc_server.Instances import Instance
from vas.tc_server.Templates import Templates
