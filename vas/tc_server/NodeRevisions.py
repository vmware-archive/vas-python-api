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

class NodeRevisions(Collection):
    """Used to enumerate revisions of a node application

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(NodeRevisions, self).__init__(client, location, 'revisions', NodeRevision)


class NodeRevision(StateResource):
    """A revision of a node application

    :ivar `vas.tc_server.NodeApplications.NodeApplication`  application:    The revision's application
    :ivar `vas.tc_server.Revisions.Revision`                revision:       The group revision that this node revision
                                                                            is a member of
    :ivar `vas.shared.Security.Security`                    security:       The resource's security
    :ivar str                                               state:          Retrieves the state of the resource from the
                                                                            server.  Will be one of:

                                                                            * ``STARTING``
                                                                            * ``STARTED``
                                                                            * ``STOPPING``
                                                                            * ``STOPPED``
    :ivar str                                               version:        The revision's version
    """

    __application = None
    __group_revision = None

    @property
    def application(self):
        self.__application = self.__application or NodeApplication(self._client, self.__application_location)
        return self.__application

    @property
    def group_revision(self):
        self.__group_revision = self.__group_revision or Revision(self._client, self.__group_revision_location)
        return self.__group_revision

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(NodeRevision, self).__init__(client, location)

        self.__version = self._details['version']

        self.__application_location = LinkUtils.get_link_href(self._details, 'node-application')
        self.__group_revision_location = LinkUtils.get_link_href(self._details, 'group-revision')

from vas.tc_server.NodeApplications import NodeApplication
from vas.tc_server.Revisions import Revision
