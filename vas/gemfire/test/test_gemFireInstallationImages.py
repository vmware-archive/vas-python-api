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
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.gemfire.GemFireInstallationImage import GemFireInstallationImage
from vas.gemfire.GemFireInstallationImages import GemFireInstallationImages
from vas.test.StubClient import StubClient

class TestInstallationImages(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__installation_images = GemFireInstallationImages(self.__client,
            'https://localhost:8443/gemfire/v1/installation-images/')

    def test_delete(self):
        self.__installation_images.delete(
            GemFireInstallationImage(self.__client, 'https://localhost:8443/gemfire/v1/installation-images/0/'))
        self.__client.delegate.delete.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/installation-images/0/')

    def test_create(self):
        self.__client.delegate.post_multipart.return_value = 'https://localhost:8443/gemfire/v1/installation-images/0/'

        installation_image = self.__installation_images.create('2.8.0.RELEASE',
            '/tmp/vfabric-gemfire-standard-2.8.0.RELEASE.zip')

        self.assertIsInstance(installation_image, GemFireInstallationImage)
        self.__client.delegate.post_multipart.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/installation-images/',
            '/tmp/vfabric-gemfire-standard-2.8.0.RELEASE.zip', {'version': '2.8.0.RELEASE'})

    def test_attributes(self):
        self.assertIsInstance(self.__installation_images.security, Security)

    def test__create_item(self):
        self.assertIsInstance(
            self.__installation_images._create_item(self.__client,
                'https://localhost:8443/gemfire/v1/installation-images/0/'), GemFireInstallationImage)

    def test___iter__(self):
        count = 0
        #noinspection PyUnusedLocal
        for node in self.__installation_images:
            count += 1

        self.assertEqual(2, count)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__installation_images)),
            '__repr__ method has not been specified')
        eval(repr(self.__installation_images))
