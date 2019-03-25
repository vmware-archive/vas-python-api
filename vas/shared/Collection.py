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
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Collection(Resource):
    """A dynamic collection of items

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    __items = None

    def __init__(self, client, location, type, entry_class):
        self.__type = type
        self.__entry_class = entry_class
        super(Collection, self).__init__(client, location)

    def reload(self):
        """Reloads the resource's details from the server"""

        super(Collection, self).reload()
        self.__items = None

    def __iter__(self):
        self.__items = self.__items or self.__create_collection_entries()
        return iter(self.__items)

    def _create_entry(self, location):
        entry = self.__entry_class(self._client, location)

        if isinstance(entry, Deletable):
            entry._collection = self

        return entry

    def __create_collection_entries(self):
        entries_json = self._details[self.__type]
        if entries_json:
            return [self._create_entry(LinkUtils.get_self_link_href(json)) for json in entries_json]
        else:
            return []
