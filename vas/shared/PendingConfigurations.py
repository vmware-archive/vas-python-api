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


from vas.shared.MutableCollectionType import MutableCollectionType

class PendingConfigurations(MutableCollectionType):
    """An collection of pending configurations

    :ivar `vas.shared.Security` security:   The security configuration for the collection of pending configurations
    """

    __COLLECTION_KEY = 'pending-configurations'

    def __init__(self, client, location):
        super(PendingConfigurations, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, path, configuration):
        """Create a new pending configuration

        :type path:     :obj:`str`
        :param path:    The path of the pending configuration
        :type configuration:    :obj:`str`
        :param configuration:   The local path configuration file
        :rtype:         :class:`vas.shared.PendingConfiguration`
        :return:        The newly created pending configuration
        """

        location = self._client.post_multipart(self._location_self, configuration, {'path': path})
        return self._create_item(self._client, location)
