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


from vas.shared.MutableCollectionType import MutableCollectionType

class TcServerTemplates(MutableCollectionType):
    """A collection of tc Server templates

    :ivar `vas.shared.Security` security:   The security configuration for the collection of templates
    """

    __COLLECTION_KEY = 'templates'

    __REL_TEMPLATE = 'template'

    def __init__(self, client, location):
        super(TcServerTemplates, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, template_image):
        """Create a new template

        :type template_image:   :class:`vas.tc_server.TcServerTemplateImage`
        :param template_image:  The template image to use when creating this template
        :rtype:         :class:`vas.tc_server.TcServerTemplate`
        :return:        The newly created template
        """

        location = self._client.post(self._location_self, {'image': template_image._location_self},
            self.__REL_TEMPLATE)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return TcServerTemplate(client, location)

from vas.tc_server.TcServerTemplate import TcServerTemplate
