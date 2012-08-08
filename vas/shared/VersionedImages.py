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

class VersionedImages(MutableCollectionType):
    """A collection of abstract versioned images

    :ivar `vas.shared.Security` security:   The security configuration for the collection of abstract versioned images
    """

    def __init__(self, client, location, collection_key):
        super(VersionedImages, self).__init__(client, location, collection_key)

    def create(self, version, image):
        """Create a new versioned image

        :type version:  :obj:`str`
        :param version: The version of the versioned image
        :type image:    :obj:`str`
        :param image:   The local path of the versioned image
        :rtype:         :class:`vas.shared.VersionedImage`
        :return:        The newly created versioned image
        """

        location = self._client.post_multipart(self._location_self, image, {'version': version})
        return self._create_item(self._client, location)

