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

class RabbitMqGroupInstances(GroupInstances):
    """An collection of RabbitMQ group instances

    :ivar `vas.shared.Security` security:   The security configuration for the collection of group instances
    """

    __REL_GROUP_INSTANCE = 'group-instance'

    __COLLECTION_KEY = 'group-instances'

    def __init__(self, client, location):
        super(RabbitMqGroupInstances, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, name, installation):
        """Create a new group instance

        :type name:     :obj:`str`
        :param name:    The name of the group instance
        :type installation:     :class:`vas.rabbitmq.RabbitMqInstallation`
        :param installation:    The installation that the group instance should use at runtime
        :rtype:         :class:`vas.rabbitmq.RabbitMqGroupInstance`
        :return:        The newly created group instance
        """

        location = self._client.post(self._location_self, {'name': name, 'installation': installation._location_self},
            self.__REL_GROUP_INSTANCE)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return RabbitMqGroupInstance(client, location)

from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
