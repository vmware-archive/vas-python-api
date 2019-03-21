# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.gemfire.ApplicationCode import ApplicationCode
from vas.gemfire.ApplicationCodeImages import ApplicationCodeImages, ApplicationCodeImage
from vas.gemfire.PendingApplicationCodes import PendingApplicationCode
from vas.test.VasTestCase import VasTestCase

class TestApplicationCodeImages(VasTestCase):
    def test_list(self):
        self._assert_collection(
            ApplicationCodeImages(self._client, 'https://localhost:8443/gemfire/v1/application-code-images/'))

    def test_create(self):
        location = 'https://localhost:8443/gemfire/v1/application-code-images/'
        self._return_location('https://localhost:8443/gemfire/v1/application-code-images/0/')

        application_code_image = ApplicationCodeImages(self._client, location).create('/tmp/application-code-image.zip',
            'example', '1.0.0')

        self.assertIsInstance(application_code_image, ApplicationCodeImage)
        self._assert_post_multipart(location, '/tmp/application-code-image.zip',
            {'name': 'example', 'version': '1.0.0'})

    def test_detail(self):
        self._assert_item(
            ApplicationCodeImage(self._client, 'https://localhost:8443/gemfire/v1/application-code-images/0/'), [
                ('name', 'example'),
                ('size', 5673284),
                ('version', "1.0.0"),
                ('live_application_code', [
                    ApplicationCode(self._client,
                        'https://localhost:8443/gemfire/v1/groups/1/cache-server-instances/2/application-code/live/3/'),
                    ApplicationCode(self._client,
                        'https://localhost:8443/gemfire/v1/groups/4/cache-server-instances/5/application-code/live/6/')
                ]),
                ('pending_application_code', [
                    PendingApplicationCode(self._client,
                        'https://localhost:8443/gemfire/v1/groups/10/cache-server-instances/11/application-code/pending/12/'),
                    PendingApplicationCode(self._client,
                        'https://localhost:8443/gemfire/v1/groups/7/cache-server-instances/8/application-code/pending/9/')
                ])
            ])

    def test_delete(self):
        self._assert_deletable(
            ApplicationCodeImage(self._client, 'https://localhost:8443/gemfire/v1/application-code-images/0/'))
