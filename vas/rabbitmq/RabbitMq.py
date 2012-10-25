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


from vas.util.LinkUtils import LinkUtils

class RabbitMq(object):
    """The entry point to the API for administering RabbitMQ

    :ivar `vas.rabbitmq.Groups.Groups`                          groups:                 The RabbitMQ groups
    :ivar `vas.rabbitmq.InstallationImages.InstallationImages`  installation_images:    The RabbitMQ installation images
    :ivar `vas.rabbitmq.Nodes.Nodes`                            nodes:                  The RabbitMQ nodes
    :ivar `vas.rabbitmq.PluginImages.PluginImages`              plugin_images:          The RabbitMQ plugin images
    """

    @property
    def groups(self):
        return self.__groups

    @property
    def installation_images(self):
        return self.__installation_images

    @property
    def nodes(self):
        return self.__nodes

    @property
    def plugin_images(self):
        return self.__plugin_images

    def __init__(self, client, location):
        self.__client = client
        self.__location = location

        json = client.get(location)
        self.__groups = Groups(client, LinkUtils.get_link_href(json, 'groups'))
        self.__installation_images = InstallationImages(client, LinkUtils.get_link_href(json, 'installation-images'))
        self.__nodes = Nodes(client, LinkUtils.get_link_href(json, 'nodes'))
        self.__plugin_images = PluginImages(client, LinkUtils.get_link_href(json, 'plugin-images'))

    def __repr__(self):
        return "{}(client={}, location={})".format(self.__class__.__name__, self.__client, repr(self.__location))


from vas.rabbitmq.Groups import Groups
from vas.rabbitmq.InstallationImages import InstallationImages
from vas.rabbitmq.Nodes import Nodes
from vas.rabbitmq.PluginImages import PluginImages
