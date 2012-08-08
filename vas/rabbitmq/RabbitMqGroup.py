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


from vas.shared.Group import Group

class RabbitMqGroup(Group):
    """A RabbitMQ group

    :ivar `vas.rabbitmq.RabbitMqGroupInstances` instances:  The collection of instances
    :ivar `vas.rabbitmq.RabbitMqInstallations` installations:  The collection of installations
    :ivar str name: The name of the group
    :ivar list nodes: The :class:`vas.rabbitmq.RabbitMqNode` s that are members of the group
    :ivar `vas.shared.Security` security:   The security configuration for the group
    """

    __REL_GROUP_INSTANCES = 'group-instances'

    def __init__(self, client, location):
        super(RabbitMqGroup, self).__init__(client, location)

        self.instances = RabbitMqGroupInstances(self._client, self._links[self.__REL_GROUP_INSTANCES][0])

    def _create_installations(self, client, location):
        return RabbitMqInstallations(client, location)

    def _create_node(self, client, location):
        return RabbitMqNode(client, location)

from vas.rabbitmq.RabbitMqInstallations import RabbitMqInstallations
from vas.rabbitmq.RabbitMqGroupInstances import RabbitMqGroupInstances
from vas.rabbitmq.RabbitMqNode import RabbitMqNode
