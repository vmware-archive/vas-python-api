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


from vas.tc_server.TemplateImages import TemplateImages, TemplateImage
from vas.tc_server.Templates import Template
from vas.test.VasTestCase import VasTestCase


class TestTemplateImages(VasTestCase):
    def test_list(self):
        self._assert_collection(TemplateImages(self._client, 'https://localhost:8443/tc-server/v1/template-images/'))

    def test_create(self):
        location = 'https://localhost:8443/tc-server/v1/template-images/'
        self._return_location('https://localhost:8443/tc-server/v1/template-images/0/')

        template_image = TemplateImages(self._client, location).create('/tmp/template-image.zip', 'example', '1.0.0')

        self.assertIsInstance(template_image, TemplateImage)
        self._assert_post_multipart(location, '/tmp/template-image.zip', {'name': 'example', 'version': '1.0.0'})

    def test_detail(self):
        self._assert_item(TemplateImage(self._client, 'https://localhost:8443/tc-server/v1/template-images/0/'), [
            ('name', 'example'),
            ('size', 5673284),
            ('version', '1.0.0'),
            ('templates', [
                Template(self._client, 'https://localhost:8443/tc-server/v1/groups/4/installations/5/templates/6/'),
                Template(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')
            ])
        ])

    def test_delete(self):
        self._assert_deletable(TemplateImage(self._client, 'https://localhost:8443/tc-server/v1/template-images/0/'))
