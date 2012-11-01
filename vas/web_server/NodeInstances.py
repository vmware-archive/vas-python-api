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


import vas.shared.NodeInstances

class NodeInstances(vas.shared.NodeInstances.NodeInstances):
    """Used to enumerate Web Server instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(NodeInstances, self).__init__(client, location, 'node-instances', NodeInstance)


class NodeInstance(vas.shared.NodeInstances.NodeInstance):
    """A Web Server node instance

    :ivar `vas.web_server.Instances.Instance`   group_instance:         The node instance's group instance
    :ivar `vas.web_server.LiveConfigurations.LiveConfigurations`    live_configurations:    The node instance's live
                                                                                            configuration
    :ivar `vas.web_server.Logs.Logs`            logs:                   The instance's logs
    :ivar str                                   name:                   The instance's name
    :ivar `vas.web_server.Nodes.Node`           node:                   The node that contains this instance
    :ivar `vas.shared.Security.Security`        security:               The resource's security
    :ivar str                                   state:                  Retrieves the state of the resource from the
                                                                        server. Will be one of:

                                                                        * ``STARTING``
                                                                        * ``STARTED``
                                                                        * ``STOPPING``
                                                                        * ``STOPPED``
    """

    def __init__(self, client, location):
        super(NodeInstance, self).__init__(client, location, Node, Logs, Instance, 'group-instance',
            NodeLiveConfigurations)


from vas.web_server.Instances import Instance
from vas.web_server.Logs import Logs
from vas.web_server.NodeLiveConfigurations import NodeLiveConfigurations
from vas.web_server.Nodes import Node
