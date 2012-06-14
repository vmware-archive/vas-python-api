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


from vas.shared.TopLevelType import TopLevelType
from vas.vfabric.AgentImage import AgentImage
from vas.vfabric.VFabricNodes import VFabricNodes

class VFabric(TopLevelType):
    """The vFabric component of the vFabric Administration Server"""

    __REL_AGENT_IMAGE = 'agent-image'

    __ROOT_PATH = "/vfabric/v1"


    def __init__(self, client, location_stem):
        super(VFabric, self).__init__(client, location_stem.format(self.__ROOT_PATH))

    @property
    def agent_image(self):
        """Return the vFabric Administration Agent image

        :rtype:     :class:`vas.vfabric.AgentImage`
        :return:    The vFabric Administration Agent image
        """

        return AgentImage(self._client, self.__location_agent_image)

    @property
    def nodes(self):
        """Return the collection of vFabric nodes

        :rtype:     :class:`vas.vfabric.VFabricNodes`
        :return:    The collection of vFabric nodes
        """

        return VFabricNodes(self._client, self._location_nodes)

    def _initialize_attributes(self, client, location):
        super(VFabric, self)._initialize_attributes(client, location)

        self.__location_agent_image = self._links[self.__REL_AGENT_IMAGE][0]
