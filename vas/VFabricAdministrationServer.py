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
from vas.vfabric.VFabric import VFabric

class VFabricAdministrationServer:
    """Represents a `vFabric Administration Server`_.

    .. _vFabric Administration Server: http://www.vmware.com/support/pubs/vfabric-vas.html

    .. note::   This is the only type that should ever be instantiated directly.  All other types are created
                automatically based on the payloads returned from the server.

    :type host:     :obj:`str`
    :param host:    The host to connect to
    :type port:     :obj:`int`
    :param port:    The port to connect to
    :type username:     :obj:`str`
    :param username:    The username to authenticate with
    :type password:     :obj:`str`
    :param password:    The password to authenticate with
    :type client:   :class:`vas.util.Client`
    :param client:  The client to use for communication with the server. This parameter should only be used to override
                    the default ``client`` for testing.
    """

    def __init__(self, host='localhost', port=8443, username='admin', password='vmware', client=None):
        self.__location_stem = 'https://{}:{}{}'.format(host, port, '{}')

        if client is None:
            self.__client = Client(username, password)
        else:
            self.__client = client

    @property
    def vfabric(self):
        """The vFabric component of the vFabric Administration Server


        :rtype:     :class:`vas.vfabric.VFabric`
        :return:    the vFabric component of the vFabric Administration Server
        """
        return VFabric(self.__client, self.__location_stem)