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
from vas.VFabricAdministrationServer import VFabricAdministrationServer
from vas.gemfire.GemFire import GemFire
from vas.rabbitmq.RabbitMq import RabbitMq
from vas.tc_server.TcServer import TcServer
from vas.test.StubClient import StubClient
from vas.vfabric.VFabric import VFabric

class TestVFabricAdministrationServer(TestCase):
    __client = StubClient()

    def setUp(self):
        self.__client.delegate.reset_mock()
        self.__vfabric_administration_server = VFabricAdministrationServer(client=self.__client)

    def test_attributes(self):
        self.assertIsInstance(self.__vfabric_administration_server.gemfire, GemFire)
        self.assertIsInstance(self.__vfabric_administration_server.rabbitmq, RabbitMq)
        self.assertIsInstance(self.__vfabric_administration_server.tc_server, TcServer)
        self.assertIsInstance(self.__vfabric_administration_server.vfabric, VFabric)

    def test_repr(self):
        self.assertIsNone(re.match('<.* object at 0x.*>', repr(self.__vfabric_administration_server)),
            '__repr__ method has not been specified')
        eval(repr(self.__vfabric_administration_server))
