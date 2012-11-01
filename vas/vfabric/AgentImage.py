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
from vas.shared.Resource import Resource
from zipfile import ZipFile
from vas.util.LinkUtils import LinkUtils

class AgentImage(Resource):
    """Provides access to the installation image for the vFabric Administration Agent

    :ivar bytearray                         content:    The content of the agent installation image (a zip file) from
                                                        the server
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    @property
    def content(self):
        return self._client.get(self.__content_location)

    def __init__(self, client, location):
        super(AgentImage, self).__init__(client, location)

        self.__content_location = LinkUtils.get_link_href(self._details, 'content')

    def extract_to(self, location=os.curdir):
        """Downloads and extracts the agent installation image

        :param str  location:   The location to extract the agent to
        :rtype:     :obj:`str`
        :return:    The root directory of the extracted agent
        """

        permissions = list()
        with ZipFile(BytesIO(self.content), 'r') as zip_file:
            for zip_info in zip_file.infolist():
                file = zip_file.extract(zip_info, location)
                permissions.append((file, zip_info.external_attr >> 16))

        for file, permission in permissions:
            os.chmod(file, permission)

        return '{}/vfabric-administration-agent'.format(location)

    def __str__(self):
        return "<{}>".format(self.__class__.__name__)
