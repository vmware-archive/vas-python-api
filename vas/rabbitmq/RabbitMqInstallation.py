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


from vas.shared.Installation import Installation
from vas.util.LinkUtils import LinkUtils

class RabbitMqInstallation(Installation):
    """A RabbitMQ installation

    :ivar `vas.rabbitmq.RabbitMqGroup` group: The installation's parent group
    :ivar list instances: The :class:`vas.rabbitmq.RabbitMqGroupInstance` s that use this installation
    :ivar `vas.rabbitmq.RabbitMqInstallationImage` installation_image: The image the installation is based on
    :ivar `vas.shared.Security` security:   The security configuration for the type
    :ivar str version: The version of the installation
    """

    __REL_GROUP_INSTANCE = 'group-instance'

    @property
    def instances(self):
        return [RabbitMqGroupInstance(self._client, location) for location in
                LinkUtils.get_links(self._client.get(self._location_self), self.__REL_GROUP_INSTANCE)]

    def _create_group(self, client, location):
        return RabbitMqGroup(client, location)

    def _create_installation_image(self, client, location):
        return RabbitMqInstallationImage(client, location)

from vas.rabbitmq.RabbitMqGroup import RabbitMqGroup
from vas.rabbitmq.RabbitMqGroupInstance import RabbitMqGroupInstance
from vas.rabbitmq.RabbitMqInstallationImage import RabbitMqInstallationImage
