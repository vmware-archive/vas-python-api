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


from vas.shared.Type import Type

class AgentImage(Type):
    """A vFabric Administration Agent image"""

    __REL_CONTENT = 'content'

    @property
    def content(self):
        """Return the binary data making up the agent distribution

        The binary data returned is in the form of a ZIP file with Info-ZIP style permissions.

        :rtype:     ``iterable`` binary data
        :return:    The binary data making up the agent distribution
        """
        return self._client.get(self.__location_content)

    def _initialize_attributes(self, client, location):
        super(AgentImage, self)._initialize_attributes(client, location)

        self.__location_content = self._links[self.__REL_CONTENT][0]
