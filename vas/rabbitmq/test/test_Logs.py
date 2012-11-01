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


from datetime import datetime
from vas.rabbitmq.Logs import Logs, Log
from vas.rabbitmq.NodeInstances import NodeInstance
from vas.test.VasTestCase import VasTestCase

class TestLogs(VasTestCase):
    def test_list(self):
        self._assert_collection(Logs(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/'))

    def test_detail(self):
        self._assert_item(Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/'), [
            ('last_modified', datetime(2012, 5, 24, 15, 20, 56)),
            ('name', 'rabbit.log'),
            ('size', 17638),
            ('instance', lambda actual: self.assertIsInstance(actual, NodeInstance))
        ])

    def test_delete(self):
        self._assert_deletable(Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/'))

    def test_content_all(self):
        self.assertEqual('nodes-instances-logs-content\n',
            Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/').content())
        self._assert_get('https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/content/')

    def test_content_start(self):
        self.assertEqual('nodes-instances-logs-content\n',
            Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/').content(start_line=1))
        self._assert_get('https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/content/?start-line=1')

    def test_content_end(self):
        self.assertEqual('nodes-instances-logs-content\n',
            Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/').content(end_line=2))
        self._assert_get('https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/content/?end-line=2')

    def test_content_start_and_end(self):
        self.assertEqual('nodes-instances-logs-content\n',
            Log(self._client, 'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/').content(start_line=1,
                end_line=2))
        self._assert_get(
            'https://localhost:8443/rabbitmq/v1/nodes/0/instances/3/logs/4/content/?start-line=1&end-line=2')
