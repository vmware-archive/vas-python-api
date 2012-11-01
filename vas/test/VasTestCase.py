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


import inspect
import re
from unittest import TestCase
from vas.shared.Security import Security
from vas.test.StubClient import StubClient

class VasTestCase(TestCase):
    __client = StubClient()

    @property
    def _client(self):
        return self.__client

    def setUp(self):
        self.__client.delegate.reset_mock()

    def _assert_collection(self, collection, size=2):
        self.assertIsInstance(collection.security, Security)
        self.__assert_count(size, collection)
        self.__assert_repr(collection)

    def _assert_deletable(self, item):
        location = item._location
        item.delete()
        self.__client.delegate.delete.assert_called_once_with(location)

    def _assert_get(self, url):
        self._client.delegate.get.assert_called_with(url)

    def _assert_item(self, item, expected_attributes=None, assert_security=True):
        if expected_attributes:
            for name, expected in expected_attributes:
                actual = getattr(item, name)
                if inspect.isfunction(expected):
                    expected(actual)
                else:
                    self.assertEqual(expected, actual)

        if assert_security:
            self.assertIsInstance(item.security, Security)

        self.__assert_repr(item)
        self.__assert_str(item)

    def _assert_post(self, url, payload=None, rel=None):
        if rel:
            self._client.delegate.post.assert_called_once_with(url, payload, rel)
        elif payload is not None:
            self._client.delegate.post.assert_called_once_with(url, payload)
        else:
            self._client.delegate.post.assert_called_once_with(url)

    def _assert_post_multipart(self, url, content, metadata=None):
        self._client.delegate.post_multipart.assert_called_once_with(url, content, metadata)

    def _return_location(self, location):
        self._client.delegate.post.return_value = location
        self._client.delegate.post_multipart.return_value = location

    def __assert_count(self, expected_count, collection):
        count = 0
        #noinspection PyUnusedLocal
        for item in collection:
            count += 1

        self.assertEqual(expected_count, count)

    def __assert_repr(self, item):
        eval_globals = None
        eval_locals = None

        for candidate in inspect.stack():
            if candidate[3].startswith('test_'):
                frame = candidate[0]
                eval_globals = dict(frame.f_globals, **globals())
                eval_locals = dict(frame.f_locals, **locals())
                break

        self.assertIsNone(re.match('<.* object at 0x.*>', repr(item)), '__repr__ method has not been specified')
        eval(repr(item), eval_globals, eval_locals)

    def __assert_str(self, item):
        self.assertNotEqual(repr(item), str(item))
