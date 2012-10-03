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
    """An error resulting from interaction with the vFabric Administration Server

    :type messages:     A variable number of :obj:`str`
    :param messages:    The messages to be displayed
    :type code:     :obj:`str`
    :param code:    The status code of the response that caused the error
    """

    def __init__(self, messages, code=None):
        super(VFabricAdministrationServerError, self).__init__()

        self.messages = []
        if isinstance(messages, list):
            self.messages.extend(messages)
        else:
            self.messages.append(messages)

        self.code = code

    def __str__(self):
        return '{}: {}'.format(self.code, ', '.join(self.messages))

    def __repr__(self):
        return '{}([{}], code={})'.format(self.__class__.__name__, ','.join(map(lambda x: repr(x), self.messages)),
            self.code)
