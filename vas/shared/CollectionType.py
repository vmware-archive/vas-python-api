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
from vas.shared.Type import Type
from vas.util.LinkUtils import LinkUtils

class CollectionType(Type):
    """An abstract collection type

    :ivar `vas.shared.Security` security:   The security configuration for the collection
    """

    def __init__(self, client, location, collection_key):
        super(CollectionType, self).__init__(client, location)

        self.__collection_key = collection_key

    def _create_item(self, client, location):
        raise VFabricAdministrationServerError('_create_item(self, client, location) method is unimplemented')

    def __iter__(self):
        return iter([self._create_item(self._client, self_location) for self_location in
                     LinkUtils.get_collection_self_links(self._details, self.__collection_key)])
