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

class ApplicationCode(Resource):
    """Application code in a cache server instance

    :ivar `vas.gemfire.ApplicationCodeImages.ApplicationCodeImage`  application_code_image: The image that was used to
                                                                                            create the application code
    :ivar `vas.gemfire.CacheServerInstances.CacheServerInstance`    instance:               The cache server instance
                                                                                            that contains the
                                                                                            application code
    :ivar str                                                       name:                   The name of the application
                                                                                            code
    :ivar `vas.shared.Security.Security`                            security:               The resource's security
    :ivar str                                                       version:                The version of the
                                                                                            application code
    """

    __application_code_image = None
    __instance = None

    @property
    def application_code_image(self):
        self.__application_code_image = self.__application_code_image or ApplicationCodeImage(self._client,
            self.__application_code_image_location)
        return self.__application_code_image

    @property
    def instance(self):
        self.__instance = self.__instance or CacheServerInstance(self._client, self.__instance_location)
        return self.__instance

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(ApplicationCode, self).__init__(client, location)

        self.__name = self._details['name']
        self.__version = self._details['version']

        self.__application_code_image_location = LinkUtils.get_link_href(self._details, 'application-code-image')
        self.__instance_location = LinkUtils.get_link_href(self._details, 'cache-server-group-instance')

    def __str__(self):
        return "<{} name={} version={}>".format(self.__class__.__name__, self.__name, self.__version)


from vas.gemfire.ApplicationCodeImages import ApplicationCodeImage
from vas.gemfire.CacheServerInstances import CacheServerInstance
