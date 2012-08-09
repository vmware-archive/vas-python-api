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


from vas.util.Client import Client
from vas.gemfire.GemFire import GemFire
from vas.rabbitmq.RabbitMq import RabbitMq
from vas.tc_server.TcServer import TcServer
from vas.vfabric.VFabric import VFabric

class VFabricAdministrationServer:
    """Represents a `vFabric Administration Server`_.

    .. _vFabric Administration Server: http://www.vmware.com/support/pubs/vfabric-vas.html

    .. note::   This is the only type that should ever be instantiated directly.  All other types are created
                automatically based on the payloads returned from the server.

    :ivar `vas.gemfire.GemFire` gemfire:   The GemFire component of the vFabric Administration Server
    :ivar `vas.rabbitmq.RabbitMq` rabbitmq:   The RabbitMQ component of the vFabric Administration Server
    :ivar `vas.tc_server.TcServer` tc_server:   The tc Server component of the vFabric Administration Server
    :ivar `vas.vfabric.VFabric` vfabric:    The vFabric component of the vFabric Administration Server

    :type host:     :obj:`str`
    :param host:    The host to connect to
    :type port:     :obj:`int`
    :param port:    The port to connect to
    :type username:     :obj:`str`
    :param username:    The username to authenticate with
    :type password:     :obj:`str`
    :param password:    The password to authenticate with
    """

    def __init__(self, host='localhost', port=8443, username='admin', password='vmware', client=None):
        if client is None:
            client = Client(username, password)

        location_stem = 'https://{}:{}{}'.format(host, port, '{}')
        self.gemfire = GemFire(client, location_stem)
        self.rabbitmq = RabbitMq(client, location_stem)
        self.tc_server = TcServer(client, location_stem)
        self.vfabric = VFabric(client, location_stem)

        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__client = client

    def __repr__(self):
        return "{}(host={}, port={}, username={}, password={}, client={})".format(self.__class__.__name__,
            repr(self.__host), self.__port, repr(self.__username), repr(self.__password), self.__client)
