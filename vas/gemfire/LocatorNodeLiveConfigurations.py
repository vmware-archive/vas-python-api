# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.shared.Collection import Collection
from vas.shared.NodeConfiguration import NodeConfiguration

class LocatorNodeLiveConfigurations(Collection):
    """Used to enumerate a locator node instance's live configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorNodeLiveConfigurations, self).__init__(client, location, 'node-live-configurations',
            LocatorNodeLiveConfiguration)


class LocatorNodeLiveConfiguration(NodeConfiguration):
    """A live configuration file in a locator node instance

    :ivar str                                                       content:    The configuration's content
    :ivar `vas.gemfire.LocatorLiveConfigurations.LocatorLiveConfiguration`  group_configuration:    The node
                                                                                                    configuration's
                                                                                                    group configuration
    :ivar `vas.gemfire.LocatorNodeInstances.LocatorNodeInstance`    instance:   The instance the owns the configuration
    :ivar str                                                       path:       The configuration's path
    :ivar `vas.shared.Security.Security`                            security:   The resource's security
    :var int                                                        size:       The configuration's size
    """

    def __init__(self, client, location):
        super(LocatorNodeLiveConfiguration, self).__init__(client, location, 'locator-node-instance',
            LocatorNodeInstance, LocatorLiveConfiguration)


from vas.gemfire.LocatorLiveConfigurations import LocatorLiveConfiguration
from vas.gemfire.LocatorNodeInstances import LocatorNodeInstance
