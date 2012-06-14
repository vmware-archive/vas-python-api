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


class Security:
    """The security configuration for an item or collection

    :ivar str owner: The owner of the item or collection
    :ivar str group:   The group of the item or collection
    :ivar dict permissions: The permissions of the item or collection. This :obj:`dict` contains keys of ``owner``,
                            ``group``, and ``other``.  The value for any of those keys is a :obj:`list` which contains
                            any of ``READ``, ``WRITE``, and ``EXECUTE``.  For example::

                                {
                                    'owner': ['READ', 'WRITE', 'EXECUTE'],
                                    'group': ['READ', 'WRITE'],
                                    'other': ['READ']
                                }
    """

    __KEY_GROUP = 'group'

    __KEY_OWNER = 'owner'

    __KEY_PERMISSIONS = 'permissions'

    def __init__(self, client, location):
        self.__client = client
        self.__location_self = location

        self._initialize_attributes(client, location)

    def update(self, owner=None, group=None, permissions=None):
        """Update this security configuration

        All elements are optional and any that are not specified will be unchanged.

        .. note:: The contents of this instance are synchronized with the server after the operation is completed.

        :type owner:    :obj:`str`
        :param owner:   The owner of the item or collection
        :type group:    :obj:`str`
        :param group:   The group of the item or collection
        :type permissions:  :obj:`dict`
        :param permissions: The permissions of the item or collection. This :obj:`dict` can only contain keys of
                            ``owner``, ``group``, and ``other``.  The value for any of those keys must be a :obj:`list`
                            which can only contain ``READ``, ``WRITE``, and ``EXECUTE``.  For example::

                                {
                                    'owner': ['READ', 'WRITE', 'EXECUTE'],
                                    'group': ['READ', 'WRITE'],
                                    'other': ['READ']
                                }
        """

        payload = dict()

        if owner is not None:
            payload[self.__KEY_OWNER] = owner

        if group is not None:
            payload[self.__KEY_GROUP] = group

        if permissions is not None:
            payload[self.__KEY_PERMISSIONS] = permissions

        self.__client.post(self.__location_self, payload)
        self._initialize_attributes(self.__client, self.__location_self)

    def _initialize_attributes(self, client, location):
        details = client.get(location)
        self.group = details[self.__KEY_GROUP]
        self.owner = details[self.__KEY_OWNER]
        self.permissions = details[self.__KEY_PERMISSIONS]

    def __eq__(self, other):
        return self.__location_self == other.__location_self

    def __hash__(self):
        return hash(self.__location_self)

    def __lt__(self, other):
        return self.__location_self < other.__location_self