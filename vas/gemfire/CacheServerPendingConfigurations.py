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


from vas.shared.PendingConfigurations import PendingConfigurations, PendingConfiguration

class CacheServerPendingConfigurations(PendingConfigurations):
    """Used to enumerate a cache server instance's pending configuration

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(CacheServerPendingConfigurations, self).__init__(client, location, CacheServerPendingConfiguration)


class CacheServerPendingConfiguration(PendingConfiguration):
    """A cache server configuration file that is pending

    :ivar str                                                       content:    The configuration's content
    :ivar `vas.gemfire.CacheServerInstances.CacheServerInstance`    instance:   The instance that owns the configuration
    :ivar str                                                       path:       The configuration's path
    :ivar `vas.shared.Security.Security`                            security:   The resource's security
    :ivar int                                                       size:       The configuration's size
    """

    def __init__(self, client, location):
        super(CacheServerPendingConfiguration, self).__init__(client, location, 'cache-server-group-instance',
            CacheServerInstance)


from vas.gemfire.CacheServerInstances import CacheServerInstance
