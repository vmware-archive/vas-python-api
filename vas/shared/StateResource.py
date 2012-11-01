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


from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class StateResource(Resource):
    """A resource that has state, i.e. it can be started and stopped and its state can be queried

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar str                               state:      Retrieves the state of the resource from the server.  Will be
                                                        one of:

                                                        * ``STARTING``
                                                        * ``STARTED``
                                                        * ``STOPPING``
                                                        * ``STOPPED``
    """

    @property
    def state(self):
        return self._client.get(self.__state_location)['status']

    def __init__(self, client, location):
        super(StateResource, self).__init__(client, location)
        self.__state_location = LinkUtils.get_link_href(self._details, 'state')

    def start(self):
        """Starts the resource"""

        self._client.post(self.__state_location, {'status': 'STARTED'})

    def stop(self):
        """Stops the resource"""

        self._client.post(self.__state_location, {'status': 'STOPPED'})
