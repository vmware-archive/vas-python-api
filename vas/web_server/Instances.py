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


import vas.shared.Instance
from vas.shared.MutableCollection import MutableCollection

class Instances(MutableCollection):
    """Used to enumerate, create, and delete Web Server instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Instances, self).__init__(client, location, 'group-instances', Instance)

    def create(self, installation, name, properties=None):
        """Creates a new instance

        :param `vas.web_server.Installations.Installation`  installation:   The installation to be used by the instance
        :param str                                          name:           The name of the instance
        :param dict                                         properties:     Optional properties to use when creating the
                                                                            instance
        :rtype:     :class:`vas.web_server.Instances.Instance`
        :return:    The new instance
        """

        payload = {'installation': installation._location, 'name': name}

        if properties:
            payload['properties'] = properties

        return self._create(payload, 'group-instance')


class Instance(vas.shared.Instance.Instance):
    """A Web Server instance

    :ivar `vas.web_server.Groups.Group`                 group:          The group that contains this instance
    :ivar `vas.web_server.Installations.Installation`   installation:   The installation that this instance is using
    :ivar `vas.web_server.LiveConfigurations.LiveConfigurations`    live_configurations:    The instance's live
                                                                                            configurations
    :ivar str                                           name:           The instance's name
    :ivar list                                          node_instances: The instance's individual node instances
    :ivar `vas.web_server.PendingConfigurations.PendingConfigurations`  pending_configurations: The instance's pending
                                                                                                configurations
    :ivar `vas.shared.Security.Security`                security:       The resource's security
    :ivar str                                           state:          Retrieves the state of the resource from the
                                                                        server. Will be one of:

                                                                        * ``STARTING``
                                                                        * ``STARTED``
                                                                        * ``STOPPING``
                                                                        * ``STOPPED``
    """

    def __init__(self, client, location):
        super(Instance, self).__init__(client, location, Group, Installation, LiveConfigurations, PendingConfigurations,
            NodeInstance, 'node-instance')

    def update(self, installation):
        """Updates the installation used by the instance

        :param `vas.web_server.Installations.Installation`  installation:   The installation to be used by the instance
        """

        payload = {'installation': installation._location}
        self._client.post(self._location, payload)
        self.reload()


from vas.web_server.Groups import Group
from vas.web_server.Installations import Installation
from vas.web_server.LiveConfigurations import LiveConfigurations
from vas.web_server.NodeInstances import NodeInstance
from vas.web_server.PendingConfigurations import PendingConfigurations
