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


from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.StateResource import StateResource
from vas.util.LinkUtils import LinkUtils

class Revisions(MutableCollection):
    """Used to enumerate, create, and delete application revisions

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location):
        super(Revisions, self).__init__(client, location, 'revisions', Revision)

    def create(self, revision_image):
        """Creates a revision by deploying the revision image

        :param `vas.tc_server.RevisionImages.RevisionImage` revision_image: The revision image to deploy
        :rtype:     :class:`vas.tc_server.Revisions.Revision`
        :return:    The new revision
        """

        return self._create({'image': revision_image._location}, 'group-revision')


class Revision(StateResource, Deletable):
    """A revision of an application

    :ivar `vas.tc_server.Applications.Application`      application:    The revision's application
    :ivar list                                          node_revisions: The revision's node revisions
    :ivar `vas.tc_server.RevisionImages.RevisionImage`  revision_image: The revision image, if any, that was used to
                                                                        create the revision
    :ivar `vas.shared.Security.Security`                security:       The resource's security
    :ivar str                                           state:          Retrieves the state of the resource from the
                                                                        server. Will be one of:

                                                                        * ``STARTING``
                                                                        * ``STARTED``
                                                                        * ``STOPPING``
                                                                        * ``STOPPED``
    :ivar str                                           version:        The revision's version
    """

    __application = None
    __node_revisions = None
    __revision_image = None

    @property
    def application(self):
        self.__application = self.__application or Application(self._client, self.__application_location)
        return self.__application

    @property
    def node_revisions(self):
        self.__node_revisions = self.__node_revisions or self._create_resources_from_links('node-revision',
            NodeRevision)
        return self.__node_revisions

    @property
    def revision_image(self):
        self.__revision_image = self.__revision_image or RevisionImage(self._client,
            self.__revision_image_location) if self.__revision_image_location else None
        return self.__revision_image

    @property
    def version(self):
        return self.__version

    def __init__(self, client, location):
        super(Revision, self).__init__(client, location)

        self.__version = self._details['version']

        self.__application_location = LinkUtils.get_link_href(self._details, 'group-application')
        self.__revision_image_location = LinkUtils.get_link_href(self._details, 'revision-image')

    def __str__(self):
        return "<{} version={}>".format(self.__class__.__name__, self.__version)


from vas.tc_server.Applications import Application
from vas.tc_server.NodeRevisions import NodeRevision
from vas.tc_server.RevisionImages import RevisionImage
