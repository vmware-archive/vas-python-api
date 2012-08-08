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

class RabbitMqPluginImages(MutableCollectionType):
    """A collection of plugin images

    :ivar `vas.shared.Security` security:   The security configuration for the collection of plugin images
    """

    __COLLECTION_KEY = 'plugin-images'

    def __init__(self, client, location):
        super(RabbitMqPluginImages, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, image):
        """Create a new plugin image

        :type image:    :obj:`str`
        :param image:   The local path of the named image
        :rtype:         :class:`vas.rabbitmq.RabbitMqPluginImage`
        :return:        The newly created plugin image
        """

        location = self._client.post_multipart(self._location_self, image)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return RabbitMqPluginImage(client, location)

from vas.rabbitmq.RabbitMqPluginImage import RabbitMqPluginImage
