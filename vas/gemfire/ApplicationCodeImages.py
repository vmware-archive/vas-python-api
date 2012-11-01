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

class ApplicationCodeImages(MutableCollection):
    """Used to enumerate, create, and delete GemFire application code images

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(ApplicationCodeImages, self).__init__(client, location, 'application-code-images', ApplicationCodeImage)

    def create(self, path, name, version):
        """Creates a new application code image by uploading a file and assigning it a name and version

        :param str  path:       The path of the file to upload
        :param str  name:       The name of the application code
        :param str  version:    The version of the application code
        :rtype:     :class:`vas.gemfire.ApplicationCodeImages.ApplicationCodeImage`
        :return:    The new application code image
        """

        return self._create_multipart(path, {'name': name, 'version': version})


class ApplicationCodeImage(Resource, Deletable):
    """An application code image

    :ivar list                              live_application_code:      The live application code that has been created
                                                                        from this application code image
    :ivar str                               name:                       The application code image's name
    :ivar list                              pending_application_code:   The pending application code that has been
                                                                        created from this application code image
    :ivar `vas.shared.Security.Security`    security:                   The resource's security
    :ivar int                               size:                       The application code image's size
    :ivar str                               version:                    The application code image's version
    """

    @property
    def live_application_code(self):
        self.__live_application_codes = self.__live_application_codes or self._create_resources_from_links(
            'live-application-code', ApplicationCode)
        return self.__live_application_codes

    @property
    def name(self):
        return self.__name

    @property
    def pending_application_code(self):
        self.__pending_application_codes = self.__pending_application_codes or self._create_resources_from_links(
            'pending-application-code', PendingApplicationCode)
        return self.__pending_application_codes

    @property
    def size(self):
        return self.__size

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(ApplicationCodeImage, self).__init__(client, location)

        self.__name = self._details['name']
        self.__size = self._details['size']
        self.__version = self._details['version']

    def reload(self):
        """Reloads the application code image's details from the server"""

        super(ApplicationCodeImage, self).reload()

        self.__live_application_codes = None
        self.__pending_application_codes = None

    def __str__(self):
        return "<{} name={} version={} size={}>".format(self.__class__.__name__, self.__name, self.__version,
            self.__size)


from vas.gemfire.ApplicationCode import ApplicationCode
from vas.gemfire.PendingApplicationCodes import PendingApplicationCode
