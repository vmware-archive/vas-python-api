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


from vas.shared.GroupInstances import GroupInstances

class GemFireCacheServerGroupInstances(GroupInstances):
    """An collection of GemFire cache server group instances

    :ivar `vas.shared.Security` security:   The security configuration for the collection of cache server group instances
    """

    __REL_CACHE_SERVER_GROUP_INSTANCE = 'cache-server-group-instance'

    __COLLECTION_KEY = 'cache-server-group-instances'

    def __init__(self, client, location):
        super(GemFireCacheServerGroupInstances, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, name, installation):
        """Create a new cache server group instance

        :type name:     :obj:`str`
        :param name:    The name of the cache server group instance
        :type installation:     :class:`vas.gemfire.GemFireInstallation`
        :param installation:    The installation that the cache server group instance should use at runtime
        :rtype:         :class:`vas.gemfire.GemFireCacheServerGroupInstance`
        :return:        The newly created cache server group instance
        """

        location = self._client.post(self._location_self, {'name': name, 'installation': installation._location_self},
            self.__REL_CACHE_SERVER_GROUP_INSTANCE)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return GemFireCacheServerGroupInstance(client, location)

from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
