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


from vas.shared.CollectionType import CollectionType

class TcServerNodeApplications(CollectionType):
    """A collection of tc Server node application

    :ivar `vas.shared.Security` security:   The security configuration for the collection of node applications
    """

    __COLLECTION_KEY = 'applications'

    def __init__(self, client, location):
        super(TcServerNodeApplications, self).__init__(client, location, self.__COLLECTION_KEY)

    def _create_item(self, client, location):
        return TcServerNodeApplication(client, location)

from vas.tc_server.TcServerNodeApplication import TcServerNodeApplication
