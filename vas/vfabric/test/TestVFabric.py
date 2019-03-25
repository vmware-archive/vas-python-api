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


from vas.test.VasTestCase import VasTestCase
from vas.vfabric.AgentImage import AgentImage
from vas.vfabric.VFabric import VFabric
from vas.vfabric.Nodes import Nodes

class TestVFabric(VasTestCase):
    def test_vfabric(self):
        self._assert_item(VFabric(self._client, 'https://localhost:8443/vfabric/v1/'), [
            ('agent_image', lambda actual: self.assertIsInstance(actual, AgentImage)),
            ('nodes', lambda actual: self.assertIsInstance(actual, Nodes))
        ], False)
