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
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.web_server.WebServer import WebServer

class VFabricAdministrationServer(object):
    """The main entry point to the vFabric Administration Server API

    :ivar `vas.gemfire.GemFire.GemFire`         gemfire:    The GemFire API
    :ivar `vas.rabbitmq.RabbitMq.RabbitMq`      rabbitmq:   The RabbitMQ API
    :ivar `vas.sqlfire.SqlFire.SqlFire`         sqlfire:    The SQLFire API, or :obj:`None` if the server is not version
                                                            1.1.0 or later
    :ivar `vas.tc_server.TcServer.TcServer`     tc_server:  The tc Server API
    :ivar `vas.vfabric.vFabric.vFabric`         vfabric:    The vFabric API
    :ivar `vas.web_server.WebServer.WebServer`  web_server: The Web Server API, or :obj:`None` if the server is not
                                                            version 1.1.0 or later
    """

    @property
    def gemfire(self):
        return self.__gemfire

    @property
    def rabbitmq(self):
        return self.__rabbitmq

    @property
    def sqlfire(self):
        return self.__sqlfire

    @property
    def tc_server(self):
        return self.__tc_server

    @property
    def vfabric(self):
        return self.__vfabric

    @property
    def web_server(self):
        return self.__web_server


    def __init__(self, host='localhost', port=8443, username='admin', password='vmware', client=None):
        """Creates an entry point that will connect to a vFabric Administration Server

        :param str  host:       The username to use to authenticate with the server
        :param int  port:       The password to use to authenticate with the server
        :param str  username:   The host of the server
        :param str  password:   The HTTPS port of the server
        """

        if client is None:
            client = Client(username, password)

        self.__gemfire = GemFire(client, 'https://{}:{}/gemfire/v1/'.format(host, port))
        self.__rabbitmq = RabbitMq(client, 'https://{}:{}/rabbitmq/v1/'.format(host, port))

        sqlfire_location = 'https://{}:{}/sqlfire/v1/'.format(host, port)
        self.__sqlfire = SqlFire(client, sqlfire_location) if self.__is_available(client, sqlfire_location) else None

        self.__tc_server = TcServer(client, 'https://{}:{}/tc-server/v1/'.format(host, port))
        self.__vfabric = VFabric(client, 'https://{}:{}/vfabric/v1/'.format(host, port))

        web_server_location = 'https://{}:{}/web-server/v1/'.format(host, port)
        self.__web_server = WebServer(client, web_server_location) if self.__is_available(client,
            web_server_location) else None

        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__client = client

    def __is_available(self, client, location):
        try:
            client.get(location)
            return True
        except VFabricAdministrationServerError as e:
            if e.code == 404:
                return False
            else:
                raise

    def __repr__(self):
        return "{}(host={}, port={}, username={}, password={}, client={})".format(self.__class__.__name__,
            repr(self.__host), self.__port, repr(self.__username), repr(self.__password), self.__client)

    def __str__(self):
        return "<{}>".format(self.__class__.__name__)
