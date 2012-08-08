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


from vas.shared.ComponentType import ComponentType

class TcServer(ComponentType):
    """The tc Server component of the vFabric Administration Server

    :ivar `vas.tc_server.TcServerGroups` groups:    The collection of groups
    :ivar `vas.tc_server.TcServerInstallationImages` installation_images:  The collection of installation images
    :ivar `vas.tc_server.TcServerNodes` nodes: The collection of nodes
    :ivar `vas.tc_server.TcServerRevisionImages` revision_images: The collection of revision images
    :ivar `vas.tc_server.TcServerTemplateImages` template_images: The collection of template images
    """

    __REL_REVISION_IMAGES = 'revision-images'

    __REL_TEMPLATE_IMAGES = 'template-images'

    __ROOT_PATH = '/tc-server/v1/'

    def __init__(self, client, location_stem):
        super(TcServer, self).__init__(client, location_stem.format(self.__ROOT_PATH))

        self.revision_images = TcServerRevisionImages(client, self._links[self.__REL_REVISION_IMAGES][0])
        self.template_images = TcServerTemplateImages(client, self._links[self.__REL_TEMPLATE_IMAGES][0])
        self.__location_stem = location_stem

    def _create_groups(self, client, location):
        return TcServerGroups(client, location)

    def _create_installation_images(self, client, location):
        return TcServerInstallationImages(client, location)

    def _create_nodes(self, client, location):
        return TcServerNodes(client, location)

    def __repr__(self):
        return "{}(client={}, location_stem={})".format(self.__class__.__name__, self._client,
            repr(self.__location_stem))

from vas.tc_server.TcServerInstallationImages import TcServerInstallationImages
from vas.tc_server.TcServerRevisionImages import TcServerRevisionImages
from vas.tc_server.TcServerGroups import TcServerGroups
from vas.tc_server.TcServerNodes import TcServerNodes
from vas.tc_server.TcServerTemplateImages import TcServerTemplateImages
