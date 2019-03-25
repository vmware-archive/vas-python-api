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


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Groups(MutableCollection):
    """A collection of groups

    :ivar `vas.shared.Security.Security`    security:   The security configuration for the collection
    """

    def __init__(self, client, location, group_class):
        super(Groups, self).__init__(client, location, 'groups', group_class)

    def create(self, name, nodes):
        """Creates a new group

        :param str  name:   The group's name
        :param list nodes:  The group's nodes
        :rtype:     :class:`vas.shared.Groups.Group`
        :return:    The new group
        """

        payload = {'name': name, 'nodes': [node._location for node in nodes]}
        return self._create(payload, 'group')


class Group(Resource, Deletable):
    """A collection of one or more nodes

    :ivar `vas.shared.Installations.Installations`  installations:  The group's installations
    :ivar str                                       name:           The group's name
    :ivar list                                      nodes:          The group's nodes
    :ivar `vas.shared.Security`                     security:       The resource's security
    """

    __installations = None
    __nodes = None

    @property
    def name(self):
        return self.__name

    @property
    def installations(self):
        self.__installations = self.__installations or self.__installations_class(self._client,
            self.__installations_location)
        return self.__installations

    @property
    def nodes(self):
        self.__nodes = self.__nodes or self._create_resources_from_links('node', self.__nodes_class)
        return self.__nodes

    def __init__(self, client, location, nodes_class, installations_class):
        super(Group, self).__init__(client, location)

        self.__installations_class = installations_class
        self.__nodes_class = nodes_class

        self.__installations_location = LinkUtils.get_link_href(self._details, 'installations')

        self.__name = self._details['name']

    def reload(self):
        """Reloads the group's details from the server"""

        super(Group, self).reload()
        self.__nodes = None

    def __str__(self):
        return "<{} name={}>".format(self.__class__.__name__, self.__name)


class MutableGroup(Group):
    """A group that supports changes to it membership

    :ivar `vas.shared.Installations.Installations`  installations:  The group's installations
    :ivar str                                       name:           The group's name
    :ivar list                                      nodes:          The group's nodes
    :ivar `vas.shared.Security`                     security:       The resource's security
    """

    def update(self, nodes):
        """Update the group to contain the given nodes

        :param  list    nodes: The group's nodes
        """

        node_locations = [node._location for node in nodes]
        self._client.post(self._location, {'nodes': node_locations})
        self.reload()


