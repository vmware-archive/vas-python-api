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

from datetime import datetime
from vas.VFabricAdministrationServerError import VFabricAdministrationServerError
from vas.shared.Type import Type

class Log(Type):
    """An abstract log

    :ivar `datetime.datetime` last_modified: The time the log file was last modified
    :ivar str name: The name of the log
    :ivar `vas.shared.NodeInstance` instance: The log's parent node instance
    :ivar int size: The size of the log
    :ivar `vas.shared.Security` security: The security configuration for the group
    """

    __KEY_LAST_MODIFIED = 'last-modified'

    __KEY_NAME = 'name'

    __KEY_SIZE = 'size'

    __REL_CONTENT = 'content'

    def __init__(self, client, location, node_instance_rel):
        super(Log, self).__init__(client, location)

        self.__location_content = self._links[self.__REL_CONTENT][0]

        self.instance = self._create_node_instance(client, self._links[node_instance_rel][0])
        self.name = self._details[self.__KEY_NAME]

    @property
    def last_modified(self):
        return datetime.utcfromtimestamp(self._client.get(self._location_self)[self.__KEY_LAST_MODIFIED])

    @property
    def size(self):
        return self._client.get(self._location_self)[self.__KEY_SIZE]

    def content(self, start_line=None, end_line=None):
        """Get the content of the log

        :type start_line:   :obj:`int`
        :param start_line:  The start point, in lines, of the content to return. A value of :obj:`None` will result in
                            content from the start of the file being returned. If the provided value is greater than
                            the number of lines in the file, the returned content will be empty.
        :type end_line:     :obj:`int`
        :param end_line:    The end point, in lines, of the content to return. A value of :obj:`None` will result in
                            content up to the end of the file being returned. If the provided value is greater than the
                            number of lines in the file, content up to and including the last line in the file will be
                            returned.
        :rtype:         :obj:`str`
        :return:        The root directory of the extracted agent
        """

        url = self.__location_content

        if start_line is not None or end_line is not None:
            url += '?'

        if start_line is not None:
            url += "start-line=" + start_line

        if start_line is not None and end_line is not None:
            url += '&'

        if end_line is not None:
            url += "end-line=" + end_line

        return self._client.get(url)

    def _create_node_instance(self, client, location):
        raise VFabricAdministrationServerError('_create_node_instance(self, client, location) method is unimplemented')
