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


from vas.shared.GroupInstances import GroupInstances

class TcServerGroupInstances(GroupInstances):
    """An collection of tc Server group instances

    :ivar `vas.shared.Security` security:   The security configuration for the collection of group instances
    """

    __REL_GROUP_INSTANCE = 'group-instance'

    __COLLECTION_KEY = 'group-instances'

    def __init__(self, client, location):
        super(TcServerGroupInstances, self).__init__(client, location, self.__COLLECTION_KEY)

    def create(self, name, installation, layout=None, properties=None, runtime_version=None, templates=None):
        """Create a new group instance

        :type name:     :obj:`str`
        :param name:    The name of the group instance
        :type installation:     :class:`vas.tc_server.TcServerInstallation`
        :param installation:    The installation that the group instance should use at runtime
        :type layout:   :obj:`str`
        :param layout:  The layout to use when creating the group instance. Valid values are ``COMBINED`` and ``SEPARATE``. The default is ``SEPARATE``
        :type properties:   :obj:`dict`
        :param properties:  The properties to use when creating the group instance
        :type runtime_version:  :obj:`str`
        :param runtime_version: The runtime version to use when creating the group instance. The default is the latest version available in the installation.
        :type templates:    :obj:`list` of :class:`vas.tc_server.TcServerTemplate`
        :param templates:   The templates to use when creating the group instance. The templates are used in the order they appear in the list.
        :rtype:         :class:`vas.tc_server.TcServerGroupInstance`
        :return:        The newly created group instance
        """

        payload = dict()
        payload['name'] = name
        payload['installation'] = installation._location_self

        if layout is not None:
            payload['layout'] = layout

        if properties is not None:
            payload['properties'] = properties

        if runtime_version is not None:
            payload['runtime-version'] = runtime_version

        if templates is not None:
            payload['templates'] = [template._location_self for template in templates]

        location = self._client.post(self._location_self, payload, self.__REL_GROUP_INSTANCE)
        return self._create_item(self._client, location)

    def _create_item(self, client, location):
        return TcServerGroupInstance(client, location)

from vas.tc_server.TcServerGroupInstance import TcServerGroupInstance
