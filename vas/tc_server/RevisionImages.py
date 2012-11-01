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


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource

class RevisionImages(MutableCollection):
    """Used to enumerate, create, and delete tc Server revision images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(RevisionImages, self).__init__(client, location, 'revision-images', RevisionImage)

    def create(self, path, name, version):
        """Creates a new revision image by uploading a war file to the server

        :param str  path:       The path of the ``.WAR`` file
        :param str  name:       The name of the revision image
        :param str  version:    The version of the revision image
        :rtype:     :class:`vas.tc_server.RevisionImages.RevisionImages`
        :return:    The new revision image
        """

        return self._create_multipart(path, {'name': name, 'version': version})


class RevisionImage(Resource, Deletable):
    """A revision image, i.e. a ``WAR`` file

    :ivar str                               name:       The revision image's name
    :ivar `vas.shared.Security.Security`    security:   The resource's security
    :ivar int                               size:       The revision image's size
    :ivar list                              revisions:  The revisions that have been created from this revision image
    :ivar str                               version:    The revision image's version
    """

    @property
    def name(self):
        return self.__name

    @property
    def revisions(self):
        self.__revisions = self.__revisions or self._create_resources_from_links('group-revision', Revision)
        return self.__revisions

    @property
    def size(self):
        return self.__size

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(RevisionImage, self).__init__(client, location)

        self.__name = self._details['name']
        self.__size = self._details['size']
        self.__version = self._details['version']

    def reload(self):
        """Reloads the revision image's details from the server"""

        super(RevisionImage, self).reload()
        self.__revisions = None

    def __str__(self):
        return "<{} name={} version={} size={}>".format(self.__class__.__name__, self.__name, self.__version,
            self.__size)


from vas.tc_server.Revisions import Revision
