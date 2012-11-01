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


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Templates(MutableCollection):
    """Used to enumerate, create, and delete tc Server templates

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Templates, self).__init__(client, location, 'templates', Template)

    def create(self, template_image):
        """Creates a new template

        :param `vas.tc_server.TemplateImages.TemplateImage` template_image: The template image to use to create the
                                                                            template
        :rtype:     :class:`vas.tc_server.Templates.Template`
        :return:    The new template
        """

        return self._create({'image': template_image._location}, 'template')


class Template(Resource, Deletable):
    """A tc Server Template

    :ivar `vas.tc_server.Installations.Installation`    installation:   The template's installation
    :ivar str                                           name:           The template's name
    :ivar `vas.shared.Security.Security`                security:       The resource's security
    :ivar `vas.tc_server.TemplateImages.TemplateImage`  template_image: The template image, if any, that this template
                                                                        was created from
    :ivar str                                           version:        The template's version
    """

    __installation = None
    __template_image = None

    @property
    def installation(self):
        self.__installation = self.__installation or Installation(self._client, self.__installation_location)
        return self.__installation

    @property
    def name(self):
        return self.__name

    @property
    def template_image(self):
        self.__template_image = self.__template_image or TemplateImage(self._client,
            self.__template_image_location) if self.__template_image_location else None
        return self.__template_image

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(Template, self).__init__(client, location)

        self.__name = self._details['name']
        self.__version = self._details['version']

        self.__installation_location = LinkUtils.get_link_href(self._details, 'installation')
        self.__template_image_location = LinkUtils.get_link_href(self._details, 'template-image')

    def __str__(self):
        return "<{} name={} version={}>".format(self.__class__.__name__, self.__name, self.__version)


from vas.tc_server.Installations import Installation
from vas.tc_server.TemplateImages import TemplateImage
