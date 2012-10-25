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


class VFabric(object):
    """The entry point of the vFabric API

    :ivar `vas.vfabric.AgentImage`  agent_image:    the installation image for the vFabric Administration agent
    :ivar `vas.vfabric.Nodes.Nodes` nodes:          the nodes that are known to the server
    """

    @property
    def agent_image(self):
        return self.__agent_image

    @property
    def nodes(self):
        return self.__nodes

    def __init__(self, client, location):
        self.__client = client
        self.__location = location

        json = client.get(location)
        self.__agent_image = AgentImage(client, LinkUtils.get_link_href(json, 'agent-image'))
        self.__nodes = Nodes(client, LinkUtils.get_link_href(json, 'nodes'))

    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location))


from vas.vfabric.AgentImage import AgentImage
from vas.vfabric.Nodes import Nodes
