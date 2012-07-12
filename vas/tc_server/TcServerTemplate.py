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

class TcServerTemplate(Type):
    """A tc Server template

    :ivar str name: The name of the template
    :ivar `vas.tc_server.TcServerInstallation` installation: The template's parent installation
    :ivar `vas.shared.Security` security:   The security configuration for the revision
    :ivar `vas.tc_server.TcServerTemplateImage` template_image: The image the template is based on
    :ivar str version:  The version of the template
    """

    __KEY_NAME = 'name'

    __KEY_VERSION = 'version'

    __REL_INSTALLATION = 'installation'

    __REL_TEMPLATE_IMAGE = 'template-image'

    def __init__(self, client, location):
        super(TcServerTemplate, self).__init__(client, location)

        self.name = self._details[self.__KEY_NAME]
        self.version = self._details[self.__KEY_VERSION]
        self.installation = TcServerInstallation(client, self._links[self.__REL_INSTALLATION][0])

        if self.__REL_TEMPLATE_IMAGE in self._links:
            self.template_image = TcServerTemplateImage(client, self._links[self.__REL_TEMPLATE_IMAGE][0])
        else:
            self.template_image = None

from vas.tc_server.TcServerInstallation import TcServerInstallation
from vas.tc_server.TcServerTemplateImage import TcServerTemplateImage
