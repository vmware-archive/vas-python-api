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


from vas.shared.Log import Log

class RabbitMqLog(Log):
    """A RabbitMQ log

    :ivar `datetime.datetime` last_modified: The time the log file was last modified
    :ivar str name: The name of the log
    :ivar `vas.rabbitmq.RabbitMqNodeInstance` instance: The log's parent node instance
    :ivar int size: The size of the log
    :ivar `vas.shared.Security` security: The security configuration for the group
    """

    __REL_NODE_INSTANCE = 'node-instance'

    def __init__(self, client, location):
        super(RabbitMqLog, self).__init__(client, location, self.__REL_NODE_INSTANCE)

    def _create_node_instance(self, client, location):
        return RabbitMqNodeInstance(client, location)

from vas.rabbitmq.RabbitMqNodeInstance import RabbitMqNodeInstance
