# vFabric Administration Server API
# Copyright (c) 2012 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from vas.gemfire.ApplicationCode import ApplicationCode
from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection

class PendingApplicationCodes(MutableCollection):
    """Used to enumerate, create, and delete a cache server's pending application code

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(PendingApplicationCodes, self).__init__(client, location, 'pending-application-code',
            PendingApplicationCode)

    def create(self, image):
        """Creates a new pending application code

        :param `vas.gemfire.ApplicationCodeImages.ApplicationCodeImage` image:  The image to create the application code
                                                                                from
        :rtype:     :class:`vas.gemfire.PendingApplicationCodes.PendingApplicationCode`
        :return:    The new application code
        """

        return self._create({'image': image._location})


class PendingApplicationCode(ApplicationCode, Deletable):
    """An application code that is pending

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
    pass
