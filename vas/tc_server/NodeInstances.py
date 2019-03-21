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


import vas.shared.NodeInstances
from vas.util.LinkUtils import LinkUtils

class NodeInstances(vas.shared.NodeInstances.NodeInstances):
    """Used to enumerate tc Server instances on an individual node

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(NodeInstances, self).__init__(client, location, 'node-instances', NodeInstance)


class NodeInstance(vas.shared.NodeInstances.NodeInstance):
    """A tc Server node instance

    :ivar `vas.tc_server.NodeApplications.NodeApplications` node_applications:  The instance's applications
    :ivar `vas.tc_server.Instances.Instance`                group_instance:     The node instance's group instance
    :ivar `vas.tc_server.LiveConfigurations.LiveConfigurations` live_configurations:    The node instance's live
                                                                                        configuration
    :ivar str                                               layout:             The instance's layout
    :ivar `vas.tc_server.Logs.Logs`                         logs:               The instance's logs
    :ivar str                                               name:               The instance's name
    :ivar `vas.tc_server.Nodes.Node`                        node:               The node that contains this instance
    :ivar str                                               runtime_version:    The version of the runtime used by the
                                                                                instance
    :ivar `vas.shared.Security.Security`                    security:           The resource's security
    :ivar dict                                              services:           The instance's services
    :ivar str                                               state:              Retrieves the state of the resource from
                                                                                the server. Will be one of:

                                                                                * ``STARTING``
                                                                                * ``STARTED``
                                                                                * ``STOPPING``
                                                                                * ``STOPPED``
    """

    __applications = None

    @property
    def applications(self):
        self.__applications = self.__applications or NodeApplications(self._client, self.__applications_location)
        return self.__applications

    @property
    def layout(self):
        return self.__layout

    @property
    def runtime_version(self):
        return self.__runtime_version

    @property
    def services(self):
        return self.__services

    def __init__(self, client, location):
        super(NodeInstance, self).__init__(client, location, Node, Logs, Instance, 'group-instance',
            NodeLiveConfigurations)

        self.__layout = self._details['layout']

        self.__applications_location = LinkUtils.get_link_href(self._details, 'node-applications')

    def reload(self):
        """Reloads the instance's details from the server"""

        super(NodeInstance, self).reload()

        self.__runtime_version = self._details['runtime-version']
        self.__services = self._details['services']


from vas.tc_server.Instances import Instance
from vas.tc_server.Logs import Logs
from vas.tc_server.NodeApplications import NodeApplications
from vas.tc_server.NodeLiveConfigurations import NodeLiveConfigurations
from vas.tc_server.Nodes import Node
