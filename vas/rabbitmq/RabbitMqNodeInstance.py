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

class RabbitMqNodeInstance(NodeInstance):
    """A RabbitMQ node instance

    :ivar `vas.rabbitmq.RabbitMqGroupInstance` group_instance: The group instance that the node instance is a member of
    :ivar `vas.rabbitmq.RabbitMqLogs` logs: The collection of logs
    :ivar str name: The name of the node instance
    :ivar `vas.rabbitmq.RabbitMqNode` node: The node instance's parent node
    :ivar `vas.shared.Security` security: The security configuration for the node instance
    :ivar str state:    The current state of the node instance.  Will be one of the following:

                        * ``STARTING``
                        * ``STARTED``
                        * ``STOPPING``
                        * ``STOPPED``
    """

    __REL_GROUP_INSTANCE = 'group-instance'

    def __init__(self, client, location):
        super(RabbitMqNodeInstance, self).__init__(client, location, self.__REL_GROUP_INSTANCE)

    def start(self):
        """Start the instance by attempting to set its ``status`` to ``STARTED``"""

        self._client.post(self._location_state, {'status': 'STARTED'})

    def _create_group_instance(self, client, location):
        return RabbitMqGroupInstance(client, location)

    def _create_logs(self, client, location):
        return RabbitMqLogs(client, location)

    def _create_node(self, client, location):
        return RabbitMqNode(client, location)

from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
from vas.rabbitmq.RabbitMqLogs import RabbitMqLogs
from vas.rabbitmq.RabbitMqNode import RabbitMqNode
