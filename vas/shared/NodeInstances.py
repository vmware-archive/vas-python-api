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
from vas.shared.StateResource import StateResource
from vas.util.LinkUtils import LinkUtils

class NodeInstances(Collection):
    """A collection of node instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    pass


class NodeInstance(StateResource):
    """A node instance, i.e. an instance on an individual node

    :ivar `vas.shared.Instance.Instance`        group_instance:         The node instance's group instance
    :ivar `vas.shared.Collection.Collection`    live_configurations:    The node instance's live configuration
    :ivar `vas.shared.Logs.Logs`                logs:                   The instance's logs
    :ivar str                                   name:                   The instance's name
    :ivar `vas.shared.Nodes.GroupableNode`      node:                   The node that contains this instance
    :ivar `vas.shared.Security.Security`        security:               The resource's security
    :ivar str                                   state:                  Retrieves the state of the resource from the
                                                                        server. Will be one of:

                                                                        * ``STARTING``
                                                                        * ``STARTED``
                                                                        * ``STOPPING``
                                                                        * ``STOPPED``
    """

    __group = None
    __live_configurations = None
    __logs = None
    __node = None

    @property
    def group_instance(self):
        self.__group = self.__group or self.__group_instance_class(self._client, self.__group_instance_location)
        return self.__group

    @property
    def live_configurations(self):
        self.__live_configurations = self.__live_configurations or self.__live_configurations_class(self._client,
            self.__live_configurations_location)
        return self.__live_configurations

    @property
    def logs(self):
        self.__logs = self.__logs or self.__logs_class(self._client, self.__logs_location)
        return self.__logs

    @property
    def name(self):
        return self.__name

    @property
    def node(self):
        self.__node = self.__node or self.__node_class(self._client, self.__node_location)
        return self.__node

    def __init__(self, client, location, node_class, logs_class, group_instance_class, group_instance_type,
                 node_live_configurations_class):
        super(NodeInstance, self).__init__(client, location)

        self.__node_class = node_class
        self.__logs_class = logs_class
        self.__group_instance_class = group_instance_class
        self.__live_configurations_class = node_live_configurations_class

        self.__node_location = LinkUtils.get_link_href(self._details, 'node')
        self.__logs_location = LinkUtils.get_link_href(self._details, 'logs')
        self.__group_instance_location = LinkUtils.get_link_href(self._details, group_instance_type)
        self.__live_configurations_location = LinkUtils.get_link_href(self._details, 'node-live-configurations')

        self.__name = self._details['name']

    def __str__(self):
        return "<{} name={}>".format(self.__class__.__name__, self.__name)
