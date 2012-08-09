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


from vas.gemfire.GemFireLiveApplicationCode import GemFireLiveApplicationCode

class GemFirePendingApplicationCode(GemFireLiveApplicationCode):
    """A pending application code

    :ivar `vas.gemfire.GemFireApplicationCodeImage` application_code_image:  The image the application code is based on
    :ivar `vas.gemfire.GemFireCacheServerGroupInstance` instance: The application code's parent group instance
    :ivar str name: The name of the application code
    :ivar `vas.shared.Security` security:   The security configuration for the type
    :ivar str version: The version of the application code
    """

    def __init__(self, client, location):
        super(GemFirePendingApplicationCode, self).__init__(client, location)
