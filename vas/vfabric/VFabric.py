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

class VFabric(TopLevelType):
    """The vFabric component of the vFabric Administration Server

    :ivar `vas.vfabric.AgentImage` agent_image: The vFabric Administration Agent image
    :ivar `vas.vfabric.VFabricNodes` nodes: The collection of nodes
    """

    __REL_AGENT_IMAGE = 'agent-image'

    __ROOT_PATH = "/vfabric/v1/"


    def __init__(self, client, location_stem):
        super(VFabric, self).__init__(client, location_stem.format(self.__ROOT_PATH))

        self.agent_image = AgentImage(client, self._links[self.__REL_AGENT_IMAGE][0])
        self.__location_stem = location_stem

    def _create_nodes(self, client, location):
        return VFabricNodes(client, location)

    def __repr__(self):
        return "{}(client={}, location_stem={})".format(self.__class__.__name__, self._client,
            repr(self.__location_stem))

from vas.vfabric.AgentImage import AgentImage
from vas.vfabric.VFabricNodes import VFabricNodes
