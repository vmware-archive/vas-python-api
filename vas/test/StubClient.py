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


import json
import os
import re
from mock import MagicMock

class StubClient:
    __LOCATION_REGEX = re.compile(
        "https://localhost:8443/(.*)/v1/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/(?:([^/]*)/)?)?)?)?)?)?)?)?)?)?")

    delegate = MagicMock()

    def get(self, location):
        self.delegate.get(location)

        captures = self.__LOCATION_REGEX.match(location).groups()
        captures = captures[:captures.index(None)]

        file_name = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'test-responses',
            captures[0]) + os.path.sep

        if len(captures) == 1:
            file_name += 'root.json'
        else:
            file_name += "-".join([capture for capture in captures[1:-1] if not None and not capture.isdigit()])
            file_name += '-' if len(captures) > 2 else ''

            final_capture = captures[-1]
            if final_capture.isdigit():
                file_name += 'detail.json'
            elif final_capture == 'state':
                file_name += 'state.json'
            elif final_capture == 'content':
                file_name += 'content'
                if os.path.exists(file_name + '.txt'):
                    file_name += '.txt'
                elif os.path.exists(file_name + '.zip'):
                    file_name += '.zip'
            else:
                file_name += final_capture + '-list.json'

        if file_name.endswith('.zip'):
            with open(file_name, 'rb') as f:
                return bytearray(f.read())
        else:
            with open(file_name) as f:
                if file_name.endswith('.json'):
                    return json.load(f)
                else:
                    return f.read()

    def delete(self, location):
        self.delegate.delete(location)

    def post(self, location, payload, rel=None):
        if rel is None:
            return self.delegate.post(location, payload)
        else:
            return self.delegate.post(location, payload, rel)

    def post_multipart(self, location, content, metadata=None):
        return self.delegate.post_multipart(location, content, metadata)

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)
