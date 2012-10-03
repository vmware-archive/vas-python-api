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


from vas.shared.LiveConfiguration import LiveConfiguration

class PendingConfiguration(LiveConfiguration):
    """A pending configuration

    :ivar `vas.shared.GroupInstance` instance: The configuration's parent group instance
    :ivar str path: The path of the configuration
    :ivar int size: The size of the configuration
    :ivar str content:  The contents of the configuration
    :ivar `vas.shared.Security` security:   The security configuration for the type
    """

    def __init__(self, client, location, group_instance_rel):
        super(PendingConfiguration, self).__init__(client, location, group_instance_rel)

    @property
    def content(self):
        return super(PendingConfiguration, self).content

    #noinspection PyMethodOverriding
    @content.setter
    def content(self, content):
        self._client.post(self._location_content, content)
