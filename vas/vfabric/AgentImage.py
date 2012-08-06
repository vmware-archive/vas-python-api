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


import os
from io import BytesIO
from vas.shared.Type import Type
from zipfile import ZipFile

class AgentImage(Type):
    """A vFabric Administration Agent image

    :ivar bytearray content: The binary data making up the agent distribution in the form of a ZIP file with Info-ZIP style permissions
    :ivar `vas.shared.Security` security:   The security configuration for the agent image
    """

    __REL_CONTENT = 'content'

    def __init__(self, client, location):
        super(AgentImage, self).__init__(client, location)

        self.__location_content = self._links[self.__REL_CONTENT][0]

    @property
    def content(self):
        return self._client.get(self.__location_content)

    def extract_to(self, location=os.curdir):
        """Extract the Administration Agent image to a specified location

        :type location:    :obj:`str`
        :param location:   The location to extract the Administration Agent image to
        :rtype:         :obj:`str`
        :return:        The root directory of the extracted agent
        """

        permissions = list()
        with ZipFile(BytesIO(self.content), 'r') as zip_file:
            for zip_info in zip_file.infolist():
                file = zip_file.extract(zip_info, location)
                permissions.append((file, zip_info.external_attr >> 16))

        for file, permission in permissions:
            os.chmod(file, permission)

        return '{}/vfabric-administration-agent'.format(location)
