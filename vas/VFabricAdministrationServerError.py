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


class VFabricAdministrationServerError(Exception):
    """Raised to indicate a failure has occurred when communicating with the vFabric Administration Server

    :ivar int   code:       the HTTP error code returned by the server
    :ivar list  messages:   the error messages, if any, returned by the server
    """

    @property
    def code(self):
        return self.__code

    @property
    def messages(self):
        return self.__messages

    def __init__(self, messages, code=None):
        self.__messages = []
        if isinstance(messages, list):
            self.__messages.extend(messages)
        else:
            self.messages.append(messages)

        self.__code = code

    def __str__(self):
        return '{}: {}'.format(self.code, ', '.join(self.messages))

    def __repr__(self):
        return '{}([{}], code={})'.format(self.__class__.__name__, ','.join(map(lambda x: repr(x), self.messages)),
            self.code)
