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


from vas.shared.Collection import Collection
from vas.shared.NodeConfiguration import NodeConfiguration

class NodeLiveConfigurations(Collection):
    """Used to enumerate a node instance's live configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(NodeLiveConfigurations, self).__init__(client, location, 'node-live-configurations',
            NodeLiveConfiguration)


class NodeLiveConfiguration(NodeConfiguration):
    """A live configuration file in a node instance

    :ivar str                                                   content:                The configuration's content
    :ivar `vas.web_server.LiveConfigurations.LiveConfiguration` group_configuration:    The node configuration's group
                                                                                        configuration
    :ivar `vas.web_server.NodeInstances.NodeInstance`           instance:               The instance the owns the
                                                                                        configuration
    :ivar str                                                   path:                   The configuration's path
    :ivar `vas.shared.Security.Security`                        security:               The resource's security
    :var int                                                    size:                   The configuration's size
    """

    def __init__(self, client, location):
        super(NodeLiveConfiguration, self).__init__(client, location, 'node-instance', NodeInstance, LiveConfiguration)


from vas.web_server.LiveConfigurations import LiveConfiguration
from vas.web_server.NodeInstances import NodeInstance
