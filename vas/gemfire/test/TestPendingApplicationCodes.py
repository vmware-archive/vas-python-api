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


from vas.gemfire.ApplicationCodeImages import ApplicationCodeImage
from vas.gemfire.CacheServerInstances import CacheServerInstance
from vas.gemfire.PendingApplicationCodes import PendingApplicationCodes, PendingApplicationCode
from vas.test.VasTestCase import VasTestCase

class TestPendingApplicationCodes(VasTestCase):
    def test_list(self):
        self._assert_collection(PendingApplicationCodes(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/'))

    def test_create(self):
        application_code_image_location = 'https://localhost:8443/gemfire/v1/application-code-images/0/'
        location = 'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/'
        self._return_location(
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/')

        pending_configuration = PendingApplicationCodes(self._client, location).create(
            ApplicationCodeImage(self._client, application_code_image_location))

        self.assertIsInstance(pending_configuration, PendingApplicationCode)
        self._assert_post(location, {'image': application_code_image_location})

    def test_detail(self):
        self._assert_item(PendingApplicationCode(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/'), [
            ('name', 'example'),
            ('version', '1.0.0'),
            ('application_code_image', lambda actual: self.assertIsInstance(actual, ApplicationCodeImage)),
            ('instance', lambda actual: self.assertIsInstance(actual, CacheServerInstance))
        ])

    def test_delete(self):
        self._assert_deletable(PendingApplicationCode(self._client,
            'https://localhost:8443/gemfire/v1/groups/0/cache-server-instances/1/application-code/pending/2/'))
