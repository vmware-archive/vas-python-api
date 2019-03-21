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


import vas.shared.Instance
from vas.shared.MutableCollection import MutableCollection
from vas.util.LinkUtils import LinkUtils


class Instances(MutableCollection):
    """Used to enumerate, create, and delete tc Server instances

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Instances, self).__init__(client, location, 'group-instances', Instance)

    def create(self, installation, name, layout=None, properties=None, runtime_version=None, templates=None):
        """Creates a new instance

        :param `vas.tc_server.Installations.Installation`   installation:       The installation to be used by the
                                                                                instance
        :param str                                          name:               The name of the instance
        :param str                                          layout:             The layout to use when creating the
                                                                                instance. Valid values are ``COMBINED``
                                                                                and ``SEPARATE``. The default is
                                                                                ``SEPARATE``.
        :param dict                                         properties:         Configuration properties that customise
                                                                                the instance
        :param str                                          runtime_version:    The version of the runtime to be used by
                                                                                the instance. Must be one of the
                                                                                ``runtime_versions`` available in the
                                                                                ``installation``. Defaults to the latest
                                                                                version that is available in the
                                                                                installation.
        :param list                                         templates:          The templates to use when creating the
                                                                                instance
        :rtype:     :class:`vas.tc_server.Instances.Instance`
        :return:    The new instance
        """

        payload = {'installation': installation._location, 'name': name}

        if layout:
            payload['layout'] = layout

        if properties:
            payload['properties'] = properties

        if runtime_version:
            payload['runtime-version'] = runtime_version

        if templates:
            payload['templates'] = [template._location for template in templates]

        return self._create(payload, 'group-instance')


class Instance(vas.shared.Instance.Instance):
    """A tc Server instance

    :ivar `vas.tc_server.Applications.Applications`     applications:       The instance's applications
    :ivar `vas.tc_server.Groups.Group`                  group:              The group that contains this instance
    :ivar `vas.tc_server.Installations.Installation`    installation:       The installation that this instance is using
    :ivar str                                           layout:             The instance's layout
    :ivar `vas.tc_server.LiveConfigurations.LiveConfiguration`  live_configurations:    The instance's live
                                                                                        configurations
    :ivar str                                           name:               The instance's name
    :ivar list                                          node_instances:     The instance's individual node instances
    :ivar `vas.tc_server.PendingConfigurations.PendingConfiguration`    pending_configurations: The instance's pending
                                                                                                configurations
    :ivar str                                           runtime_version:    The version of the runtime used by the
                                                                            instance
    :ivar `vas.shared.Security.Security`                security:           The resource's security
    :ivar dict                                          services:           The instance's services
    :ivar str                                           state:              Retrieves the state of the resource from the
                                                                            server. Will be one of:

                                                                            * ``STARTING``
                                                                            * ``STARTED``
                                                                            * ``STOPPING``
                                                                            * ``STOPPED``
    """

    __applications = None

    @property
    def applications(self):
        self.__applications = self.__applications or Applications(self._client, self.__applications_location)
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
        super(Instance, self).__init__(client, location, Group, Installation, LiveConfigurations, PendingConfigurations,
            NodeInstance, 'node-instance')

        self.__layout = self._details['layout']

        self.__applications_location = LinkUtils.get_link_href(self._details, 'group-applications')

    def reload(self):
        """Reloads the instance's details from the server"""

        super(Instance, self).reload()

        self.__runtime_version = self._details['runtime-version']
        self.__services = self._details['services']

    def update(self, installation, runtime_version=None):
        """Updates the installation and, optionally, the ``runtime_version`` used by the instance

        :param `vas.tc_server.Installations.Installation`   installation:       The installation to be used by the
                                                                                instance
        :param str                                          runtime_version:    The version of the runtime to be used by
                                                                                the instance
        """

        payload = {'installation': installation._location}
        if runtime_version:
            payload['runtime-version'] = runtime_version

        self._client.post(self._location, payload)
        self.reload()

    def __str__(self):
        return "<{} name={} layout={} runtime_version={} services={}>".format(self.__class__.__name__, self.__name,
            self.__layout, self.__runtime_version, self.__services)


from vas.tc_server.Applications import Applications
from vas.tc_server.Groups import Group
from vas.tc_server.Installations import Installation
from vas.tc_server.LiveConfigurations import LiveConfigurations
from vas.tc_server.NodeInstances import NodeInstance
from vas.tc_server.PendingConfigurations import PendingConfigurations
