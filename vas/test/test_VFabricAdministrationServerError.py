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

import re
from unittest import TestCase
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class TestVFabricAdministrationServerError(TestCase):
    def test_no_code(self):
        error = VFabricAdministrationServerError(['message1', 'message2'])
        self.assertEqual(['message1', 'message2'], error.messages)
        self.assertEqual(None, error.code)

    def test_single(self):
        error = VFabricAdministrationServerError('message1')
        self.assertEqual(['message1'], error.messages)
        self.assertEqual(None, error.code)

    def test_with_code(self):
        error = VFabricAdministrationServerError(['message1', 'message2'], code='400')
        self.assertEqual(['message1', 'message2'], error.messages)
        self.assertEqual('400', error.code)

    def test_repr(self):
        error = VFabricAdministrationServerError(['message1', 'message2'], code='400')

        self.assertIsNone(re.match('<.* object at 0x.*>', repr(error)), '__repr__ method has not been specified')
        eval(repr(error))
