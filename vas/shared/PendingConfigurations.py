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


from vas.shared.Configuration import Configuration
from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection

class PendingConfigurations(MutableCollection):
    """A collection of an instance's pending configurations

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location, entry_class):
        super(PendingConfigurations, self).__init__(client, location, 'pending-configurations', entry_class)

    def create(self, path, content):
        """Creates a new configuration. The configuration will be pending until its instance is started at which point
        the configuration will become live.

        :param str  path:       The configuration's path
        :param str  content:    The configuration's content
        :rtype:     :class:`vas.shared.PendingConfigurations.PendingConfiguration`
        :return:    The new configuration
        """

        return self._create_multipart(content, {'path': path})

class PendingConfiguration(Configuration, Deletable):
    """A configuration file that is pending and will be made live the next time its instance is started

    :ivar str                               content:    The configuration's content
    :ivar `vas.shared.Instance.Instance`    instance:   The instance that owns the configuration
    :ivar str                               path:       The configuration's path
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar int                               size:       The configuration's size
    """

    #noinspection PyMethodOverriding
    @Configuration.content.setter
    def content(self, content):
        self._client.post(self._content_location, content)
