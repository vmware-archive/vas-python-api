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


from vas.shared.Collection import Collection

class MutableCollection(Collection):
    """A collection that allows items to be created

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def _create(self, payload, rel = None):
        created = self._create_entry(self._client.post(self._location, payload, rel))
        self.reload()
        return created

    def _create_multipart(self, path, payload = None):
        created = self._create_entry(self._client.post_multipart(self._location, path, payload))
        self.reload()
        return created
