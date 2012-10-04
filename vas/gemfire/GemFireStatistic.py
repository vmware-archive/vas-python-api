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

from datetime import datetime
from vas.shared.Type import Type

class GemFireStatistic(Type):
    """A GemFire statistic

    :ivar `datetime.datetime` last_modified: The time the statistic was last modified
    :ivar `bytearray` content: The contents of the statistic
    :ivar str name: The name of the statistic
    :ivar `vas.gemfire.GemFireCacheServerNodeInstance` instance: The statistic's parent node instance
    :ivar int size: The size of the statistic
    :ivar `vas.shared.Security` security: The security configuration for the statistic
    """

    __KEY_LAST_MODIFIED = 'last-modified'

    __KEY_PATH = 'path'

    __KEY_SIZE = 'size'

    __REL_CONTENT = 'content'

    __REL_NODE_INSTANCE = 'cache-server-node-instance'

    def __init__(self, client, location):
        super(GemFireStatistic, self).__init__(client, location)

        self.__location_content = self._links[self.__REL_CONTENT][0]

        self.instance = GemFireCacheServerNodeInstance(client, self._links[self.__REL_NODE_INSTANCE][0])
        self.path = self._details[self.__KEY_PATH]

    @property
    def last_modified(self):
        return datetime.utcfromtimestamp(self._client.get(self._location_self)[self.__KEY_LAST_MODIFIED])

    @property
    def size(self):
        return self._client.get(self._location_self)[self.__KEY_SIZE]

    @property
    def content(self):
        return self._client.get(self.__location_content)

from GemFireCacheServerNodeInstance import GemFireCacheServerNodeInstance