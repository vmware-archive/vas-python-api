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


from vas.shared.NodeInstance import NodeInstance

class GemFireCacheServerNodeInstance(NodeInstance):
    """A GemFire cache server node instance

    :ivar `vas.gemfire.GemFireDiskStores` disk_stores: The collection of disk stores
    :ivar `vas.gemfire.GemFireCacheServerGroupInstance` group_instance: The group instance that the node instance is a member of
    :ivar `vas.gemfire.GemFireCacheServerLogs` logs: The collection of logs
    :ivar str name: The name of the node instance
    :ivar `vas.gemfire.GemFireNode` node: The node instance's parent node
    :ivar `vas.shared.Security` security: The security configuration for the node instance
    :ivar `vas.gemfire.GemFireStatistics` statistics: The collection of statistics
    :ivar str state:    The current state of the node instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __REL_DISK_STORES = 'disk-stores'

    __REL_STATISTICS = 'statistics'

    __REL_GROUP_INSTANCE = 'cache-server-group-instance'

    def __init__(self, client, location):
        super(GemFireCacheServerNodeInstance, self).__init__(client, location, self.__REL_GROUP_INSTANCE)

        self.disk_stores = GemFireDiskStores(client, self._links[self.__REL_DISK_STORES][0])
        self.statistics = GemFireStatistics(client, self._links[self.__REL_STATISTICS][0])

    def start(self, rebalance=None):
        """Start the instance by attempting to set its ``status`` to ``STARTED``

        :type rebalance:     :obj:`bool`
        :param rebalance:    Whether to rebalance the cache server on start
        """

        payload = dict()
        payload['status'] = 'STARTED'

        if rebalance is not None:
            payload['rebalance'] = rebalance

        self._client.post(self._location_state, payload)

    def _create_group_instance(self, client, location):
        return GemFireCacheServerGroupInstance(client, location)

    def _create_logs(self, client, location):
        return GemFireCacheServerLogs(client, location)

    def _create_node(self, client, location):
        return GemFireNode(client, location)

from vas.gemfire.GemFireCacheServerGroupInstance import GemFireCacheServerGroupInstance
from vas.gemfire.GemFireCacheServerLogs import GemFireCacheServerLogs
from vas.gemfire.GemFireDiskStores import GemFireDiskStores
from vas.gemfire.GemFireNode import GemFireNode
from vas.gemfire.GemFireStatistics import GemFireStatistics
