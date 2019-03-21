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


import vas.shared.Groups
from vas.util.LinkUtils import LinkUtils

class Groups(vas.shared.Groups.Groups):
    """Used to enumerate, create, and delete tc Server groups

    :ivar `vas.shared.Security.Security`    security:   The security configuration for the collection
    """

    def __init__(self, client, location):
        super(Groups, self).__init__(client, location, Group)


class Group(vas.shared.Groups.MutableGroup):
    """A tc Server group

    :ivar `vas.tc_server.Installations.Installations`   installations:  The group's installations
    :ivar `vas.tc_server.Instances.Instances`           instances:      The group's instances
    :ivar str                                           name:           The group's name
    :ivar list                                          nodes:          The group's nodes
    :ivar `vas.shared.Security`                         security:       The resource's security
    """

    __instances = None

    @property
    def instances(self):
        self.__instances = self.__instances or Instances(self._client, self.__instances_location)
        return self.__instances

    def __init__(self, client, location):
        super(Group, self).__init__(client, location, Node, Installations)

        self.__instances_location = LinkUtils.get_link_href(self._details, 'group-instances')

from vas.tc_server.Installations import Installations
from vas.tc_server.Instances import Instances
from vas.tc_server.Nodes import Node
