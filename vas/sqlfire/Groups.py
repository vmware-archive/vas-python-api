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


import vas.shared.Groups
from vas.util.LinkUtils import LinkUtils

class Groups(vas.shared.Groups.Groups):
    """Used to enumerate, create, and delete SqlFire groups

    :ivar `vas.shared.Security.Security`    security:   The security configuration for the collection
    """

    def __init__(self, client, location):
        super(Groups, self).__init__(client, location, Group)


class Group(vas.shared.Groups.MutableGroup):
    """A SqlFire group

    :ivar `vas.sqlfire.AgentInstances.AgentInstances`       agent_instances:    The group's agent instances
    :ivar `vas.sqlfire.Installations.Installations`         installations:      The group's installations
    :ivar `vas.sqlfire.LocatorInstances.LocatorInstances`   locator_instances:  The group's locator instances
    :ivar str                                               name:               The group's name
    :ivar list                                              nodes:              The group's nodes
    :ivar `vas.shared.Security`                             security:           The resource's security
    :ivar `vas.sqlfire.ServerInstances.ServerInstances`     server_instances:   The group's server instances
    """

    __agent_instances = None
    __server_instances = None
    __locator_instances = None

    @property
    def agent_instances(self):
        self.__agent_instances = self.__agent_instances or AgentInstances(self._client, self.__agent_instances_location)
        return self.__agent_instances

    @property
    def locator_instances(self):
        self.__locator_instances = self.__locator_instances or LocatorInstances(self._client,
            self.__locator_instances_location)
        return self.__locator_instances

    @property
    def server_instances(self):
        self.__server_instances = self.__server_instances or ServerInstances(self._client,
            self.__server_instances_location)
        return self.__server_instances

    def __init__(self, client, location):
        super(Group, self).__init__(client, location, Node, Installations)

        self.__agent_instances_location = LinkUtils.get_link_href(self._details, 'agent-group-instances')
        self.__locator_instances_location = LinkUtils.get_link_href(self._details, 'locator-group-instances')
        self.__server_instances_location = LinkUtils.get_link_href(self._details, 'server-group-instances')


from vas.sqlfire.AgentInstances import AgentInstances
from vas.sqlfire.ServerInstances import ServerInstances
from vas.sqlfire.Installations import Installations
from vas.sqlfire.LocatorInstances import LocatorInstances
from vas.sqlfire.Nodes import Node
