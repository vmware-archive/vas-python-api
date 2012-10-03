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


from vas.shared.InstallationImage import InstallationImage

class GemFireInstallationImage(InstallationImage):
    """A GemFire installation image

    :ivar list installations: The :class:`vas.gemfire.GemFireInstallation` s that use the installation image
    :ivar `vas.shared.Security` security:   The security configuration for the installation image
    :ivar int size: The size of the image
    :ivar str version: The version of the installation image
    """

    def _create_item(self, client, location):
        return GemFireInstallation(client, location)

from vas.gemfire.GemFireInstallation import GemFireInstallation
