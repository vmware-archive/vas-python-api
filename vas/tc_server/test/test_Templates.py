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


from vas.tc_server.Installations import Installation
from vas.tc_server.TemplateImages import TemplateImage
from vas.tc_server.Templates import Templates, Template
from vas.test.VasTestCase import VasTestCase

class TestTemplates(VasTestCase):
    def test_list(self):
        self._assert_collection(
            Templates(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/'), 3)

    def test_create(self):
        template_image_location = 'https://localhost:8443/tc-server/v1/template-images/0/'
        location = 'https://localhost:8443/tc-server/v1/template-images/0/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')

        template = Templates(self._client, location).create(TemplateImage(self._client, template_image_location))

        self.assertIsInstance(template, Template)
        self._assert_post(location, {'image': template_image_location}, 'template')

    def test_detail(self):
        self._assert_item(
            Template(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'), [
                ('name', 'example'),
                ('version', '1.0.0'),
                ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
                ('template_image', lambda actual: self.assertIsInstance(actual, TemplateImage))
            ])


    def test_delete(self):
        self._assert_deletable(
            Template(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'))
