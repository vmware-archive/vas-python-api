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


class Security(object):
    """The security configuration for a resource

    :ivar str   group:          the group of the resource
    :ivar str   owner:          the owner of the resource
    :ivar dict  permissions:    The permissions of the resource. This :obj:`dict` contains keys of ``owner``,
                                ``group``, and ``other``.  The value for any of those keys is a :obj:`list` which
                                contains any of ``READ``, ``WRITE``, and ``EXECUTE``.  For example:

                                .. code-block:: json

                                    {
                                        'owner': ['READ', 'WRITE', 'EXECUTE'],
                                        'group': ['READ', 'WRITE'],
                                        'other': ['READ']
                                    }

    """

    @property
    def group(self):
        return self.__group

    @property
    def owner(self):
        return self.__owner

    @property
    def permissions(self):
        return self.__permissions

    def __init__(self, client, location):
        self.__client = client
        self.__location = location

        self.reload()

    def reload(self):
        """Reloads the security configuration from the server"""

        json = self.__client.get(self.__location)
        self.__group = json['group']
        self.__owner = json['owner']
        self.__permissions = json['permissions']


    def chown(self, owner=None, group=None):
        """Change the owner and group security configuration for an item or collection. Analogous to the UNIX |chown|_
        command.

        .. |chown| replace:: ``chown``
        .. _chown: http://en.wikipedia.org/wiki/Chown

        :param str  owner:  The new owner of the item or collection.  Unchanged if :obj:`None`.
        :param str  group:  The new group of the item or collection.  Unchanged if :obj:`None`.
        """

        payload = dict()

        if owner:
            payload['owner'] = owner

        if group:
            payload['group'] = group

        self.__client.post(self.__location, payload)
        self.reload()

    def chmod(self, owner=None, group=None, other=None):
        """Change the permissions for an item or collection. Analogous to the UNIX |chmod|_ command.

        .. |chmod| replace:: ``chmod``
        .. _chmod: http://en.wikipedia.org/wiki/Chmod

        :param list owner:  The new owner class permissions of the item or collection. Legal values are any of ``READ``,
                            ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        :param list group:  The new group class permissions of the item or collection. Legal values are any of ``READ``,
                            ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        :param list other:  The new other class permissions of the item or collection. Legal values are any of ``READ``,
                            ``WRITE``, and ``EXECUTE``. Unchanged if :obj:`None`.
        """

        permissions = dict()

        if owner:
            permissions['owner'] = owner

        if group:
            permissions['group'] = group

        if other:
            permissions['other'] = other

        self.__client.post(self.__location, {'permissions': permissions})

        if owner:
            self.permissions['owner'] = owner

        if group:
            self.permissions['group'] = group

        if other:
            self.permissions['other'] = other

    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location))
