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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.util.LinkUtils import LinkUtils

class TopLevelType(object):
    """An abstract top level type

    :ivar `vas.shared.Nodes` nodes:  The collection of nodes
    """

    __REL_NODES = 'nodes'

    def __init__(self, client, location):
        self._client = client
        self._links = LinkUtils.get_links(client.get(location))

        self.nodes = self._create_nodes(client, self._links[self.__REL_NODES][0])

    def _create_nodes(self, client, location):
        raise VFabricAdministrationServerError('_create_nodes(self, client, location) method is unimplemented')
