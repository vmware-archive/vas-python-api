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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.Type import Type

class LiveConfiguration(Type):
    """A live configuration

    :ivar `vas.shared.GroupInstance` instance: The configuration's parent group instance
    :ivar str path: The path of the configuration
    :ivar int size: The size of the configuration
    :ivar str content:  The contents of the configuration
    :ivar `vas.shared.Security` security:   The security configuration for the type
    """

    __KEY_PATH = 'path'

    __KEY_SIZE = 'size'

    __REL_CONTENT = 'content'

    def __init__(self, client, location, group_instance_rel):
        super(LiveConfiguration, self).__init__(client, location)

        self.instance = self._create_group_instance(client, self._links[group_instance_rel][0])
        self.path = self._details[self.__KEY_PATH]
        self.size = self._details[self.__KEY_SIZE]

        self._location_content = self._links[self.__REL_CONTENT][0]

    @property
    def content(self):
        return self._client.get(self._location_content)

    def _create_group_instance(self, client, location):
        raise VFabricAdministrationServerError('_create_group_instance(self, client, location) method is unimplemented')
