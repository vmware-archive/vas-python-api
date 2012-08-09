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


import re
from unittest.case import TestCase
from vas.shared.Security import Security
from vas.gemfire.GemFireGroup import GemFireGroup
from vas.gemfire.GemFireAgentGroupInstance import GemFireAgentGroupInstance
from vas.gemfire.GemFireInstallation import GemFireInstallation
from vas.gemfire.GemFireAgentLiveConfigurations import GemFireAgentLiveConfigurations
from vas.gemfire.GemFireAgentNodeInstance import GemFireAgentNodeInstance
from vas.gemfire.GemFireAgentPendingConfigurations import GemFireAgentPendingConfigurations
from vas.test.StubClient import StubClient

class TestGemFireAgentGroupInstance(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__instance = GemFireAgentGroupInstance(self.__client,
            'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/')

    def test_attributes(self):
        self.assertEqual('example', self.__instance.name)
        self.assertEqual('STOPPED', self.__instance.state)
        self.assertIsInstance(self.__instance.group, GemFireGroup)
        self.assertIsInstance(self.__instance.installation, GemFireInstallation)
        self.assertIsInstance(self.__instance.live_configurations, GemFireAgentLiveConfigurations)
        self.assertEquals(
            [GemFireAgentNodeInstance(self.__client, 'https://localhost:8443/gemfire/v1/nodes/0/agent-instances/5/'),
             GemFireAgentNodeInstance(self.__client, 'https://localhost:8443/gemfire/v1/nodes/1/agent-instances/6/')],
            self.__instance.nodes_instances)
        self.assertIsInstance(self.__instance.pending_configurations, GemFireAgentPendingConfigurations)
        self.assertIsInstance(self.__instance.security, Security)

    def test_start_parallel(self):
        self.__instance.start()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/', {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        self.__instance.start(True)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/', {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        self.__instance.stop()
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/', {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        self.__instance.stop(True)
        self.__client.delegate.post.assert_called_once_with(
            'https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/state/', {'status': 'STOPPED', 'serial': True})

    def test_update(self):
        self.__client.delegate.reset_mock()
        self.__instance.update(
            GemFireInstallation(self.__client, 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'))

        self.__client.delegate.post.assert_called_once_with('https://localhost:8443/gemfire/v1/groups/2/agent-instances/4/',
                {'installation': 'https://localhost:8443/gemfire/v1/groups/1/installations/2/'})

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__instance)),
            '__repr__ method has not been specified')
        eval(repr(self.__instance))
