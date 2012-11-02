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
from vas.shared.LiveConfiguration import LiveConfiguration

class LocatorLiveConfigurations(Collection):
    """Used to enumerate a locator instance's live configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(LocatorLiveConfigurations, self).__init__(client, location, 'live-configurations',
            LocatorLiveConfiguration)


class LocatorLiveConfiguration(LiveConfiguration):
    """A live configuration file in a locator instance

    :ivar str                                               content:                The configuration's content
    :ivar `vas.sqlfire.LocatorInstances.LocatorInstance`    instance:               The instance that owns the
                                                                                    configuration
    :ivar str                                               path:                   The configuration's path
    :ivar list                                              node_configurations:    The configuration's node
                                                                                    configurations
    :ivar `vas.shared.Security.Security`                    security:               The resource's security
    :ivar int                                               size:                   The configuration's size
    """

    def __init__(self, client, location):
        super(LocatorLiveConfiguration, self).__init__(client, location, 'locator-group-instance', LocatorInstance,
            LocatorNodeLiveConfiguration)


from vas.sqlfire.LocatorInstances import LocatorInstance
from vas.sqlfire.LocatorNodeLiveConfigurations import LocatorNodeLiveConfiguration
