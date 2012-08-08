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
import os
import shutil
import tempfile
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.test.StubClient import StubClient
from vas.vfabric.AgentImage import AgentImage

class TestAgentImage(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__agent_image = AgentImage(self.__client, 'https://localhost:8443/vfabric/v1/agent-image/')

    def test_attributes(self):
        self.assertEqual(164, len(self.__agent_image.content))
        self.assertIsInstance(self.__agent_image.security, Security)

    def test_extract_to(self):
        location = tempfile.mkdtemp()
        try:
            self.__agent_image.extract_to(location)
            self.assertTrue(os.path.exists(os.path.join(location, 'foo.txt')))
        finally:
            shutil.rmtree(location)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__agent_image)),
            '__repr__ method has not been specified')
        eval(repr(self.__agent_image))
