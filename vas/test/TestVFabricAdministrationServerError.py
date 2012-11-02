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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.test.VasTestCase import VasTestCase

class TestVFabricAdministrationServerError(VasTestCase):
    def test_error(self):
        self._assert_item(VFabricAdministrationServerError(['message1', 'message2']), [
            ('code', None),
            ('messages', ['message1', 'message2'])
        ], False)

        self._assert_item(VFabricAdministrationServerError(['message1']), [
            ('code', None),
            ('messages', ['message1'])
        ], False)

        self._assert_item(VFabricAdministrationServerError(['message1', 'message2'], 400), [
            ('code', 400),
            ('messages', ['message1', 'message2'])
        ], False)
