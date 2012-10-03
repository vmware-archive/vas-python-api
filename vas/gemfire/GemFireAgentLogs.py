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


from vas.shared.Logs import Logs

class GemFireAgentLogs(Logs):
    """A collection of GemFire agent logs

    :ivar `vas.shared.Security` security:   The security configuration for the collection of logs
    """

    def _create_item(self, client, location):
        return GemFireAgentLog(client, location)

from vas.gemfire.GemFireAgentLog import GemFireAgentLog
