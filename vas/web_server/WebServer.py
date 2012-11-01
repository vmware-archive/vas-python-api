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


from vas.util.LinkUtils import LinkUtils

class WebServer(object):
    """The entry point to the API for administering vFabric Web Server

    :ivar `vas.web_server.Groups.Groups`                            groups:                 The Web Server groups
    :ivar `vas.web_server.InstallationImages.InstallationImages`    installation_images:    The Web Server installation
                                                                                            images
    :ivar `vas.web_server.Nodes.Nodes`                              nodes:                  The Web Server nodes
    """

    @property
    def groups(self):
        return self.__groups

    @property
    def installation_images(self):
        return self.__installation_images

    @property
    def nodes(self):
        return self.__nodes

    def __init__(self, client, location):
        self.__client = client
        self.__location = location

        json = client.get(location)
        self.__groups = Groups(client, LinkUtils.get_link_href(json, 'groups'))
        self.__installation_images = InstallationImages(client, LinkUtils.get_link_href(json, 'installation-images'))
        self.__nodes = Nodes(client, LinkUtils.get_link_href(json, 'nodes'))

    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location))

    def __str__(self):
        return "<{}>".format(self.__class__)


from vas.web_server.Groups import Groups
from vas.web_server.InstallationImages import InstallationImages
from vas.web_server.Nodes import Nodes
