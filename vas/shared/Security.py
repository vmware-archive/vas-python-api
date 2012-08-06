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

    :ivar str owner:    The owner of the item or collection
    :ivar str group:    The group of the item or collection
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

    __KEY_OTHER = 'other'

    __KEY_OWNER = 'owner'

    __KEY_PERMISSIONS = 'permissions'

    def __init__(self, client, location):
        self.__client = client
        self.__location_self = location

        details = client.get(location)
        self.group = details[self.__KEY_GROUP]
        self.owner = details[self.__KEY_OWNER]
        self.permissions = details[self.__KEY_PERMISSIONS]

    def chown(self, owner=None, group=None):
        """Change the owner and group security configuration for an item or collection. Analogous to the UNIX |chown|_ command.

        .. |chown| replace:: ``chown``
        .. _chown: http://en.wikipedia.org/wiki/Chown

        :type owner:     :obj:`str`
        :param owner:    The new owner of the item or collection.  Unchanged if :obj:`None`.
        :type group:     :obj:`str`
        :param group:    The new group of the item or collection.  Unchanged if :obj:`None`.
        """

        payload = dict()

        if owner is not None:
            payload[self.__KEY_OWNER] = owner

        if group is not None:
            payload[self.__KEY_GROUP] = group

        self.__client.post(self.__location_self, payload)

        if owner is not None:
            self.owner = owner

        if group is not None:
            self.group = group


    def chmod(self, owner=None, group=None, other=None):
        """Change the permissions for an item or collection. Analogous to the UNIX |chmod|_ command.

        .. |chmod| replace:: ``chmod``
        .. _chmod: http://en.wikipedia.org/wiki/Chmod

        :type owner:     :obj:`list` of :obj:`str`
        :param owner:    The new owner class permissions of the item or collection.  Legal values are any of ``READ``,
                         ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        :type group:     :obj:`list` of :obj:`str`
        :param group:    The new group class permissions of the item or collection.  Legal values are any of ``READ``,
                         ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        :type other:     :obj:`list` of :obj:`str`
        :param other:    The new other class permissions of the item or collection.  Legal values are any of ``READ``,
                         ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        """

        permissions = dict()

        if owner is not None:
            permissions[self.__KEY_OWNER] = owner

        if group is not None:
            permissions[self.__KEY_GROUP] = group

        if other is not None:
            permissions[self.__KEY_OTHER] = other

        self.__client.post(self.__location_self, {self.__KEY_PERMISSIONS: permissions})

        if owner is not None:
            self.permissions[self.__KEY_OWNER] = owner

        if group is not None:
            self.permissions[self.__KEY_GROUP] = group

        if other is not None:
            self.permissions[self.__KEY_OTHER] = other


    def __eq__(self, other):
        return self.__location_self == other.__location_self

    def __hash__(self):
        return hash(self.__location_self)

    def __lt__(self, other):
        return self.__location_self < other.__location_self

    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location_self))
