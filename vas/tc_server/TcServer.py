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

class TcServer(object):
    """The entry point to the API for administering tc Server

    :ivar `vas.tc_server.Groups.Groups`                         groups:                 the tc Server groups
    :ivar `vas.tc_server.InstallationImages.InstallationImages` installation_images:    the tc Server installation
                                                                                        images
    :ivar `vas.tc_server.Nodes.Nodes`                           nodes:                  The tc Server nodes
    :ivar `vas.tc_server.RevisionImages.RevisionImages`         revision_images:        The tc Server revision images
    :ivar `vas.tc_server.TemplateImages.TemplateImages`         template_images:        The tc Server template images
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

    @property
    def revision_images(self):
        return self.__revision_images

    @property
    def template_images(self):
        return self.__template_images

    def __init__(self, client, location):
        self.__client = client
        self.__location = location

        json = client.get(location)
        self.__groups = Groups(client, LinkUtils.get_link_href(json, 'groups'))
        self.__installation_images = InstallationImages(client, LinkUtils.get_link_href(json, 'installation-images'))
        self.__nodes = Nodes(client, LinkUtils.get_link_href(json, 'nodes'))
        self.__revision_images = RevisionImages(client, LinkUtils.get_link_href(json, 'revision-images'))
        self.__template_images = TemplateImages(client, LinkUtils.get_link_href(json, 'template-images'))


    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location))


from vas.tc_server.Groups import Groups
from vas.tc_server.InstallationImages import InstallationImages
from vas.tc_server.Nodes import Nodes
from vas.tc_server.RevisionImages import RevisionImages
from vas.tc_server.TemplateImages import TemplateImages
