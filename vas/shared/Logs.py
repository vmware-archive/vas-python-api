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
from vas.shared.Deletable import Deletable
from vas.shared.MutableCollection import MutableCollection
from vas.shared.Resource import Resource
from vas.util.LinkUtils import LinkUtils

class Logs(MutableCollection):
    """A node instance's logs

    :ivar `vas.shared.Security.Security`    security:   The resource's security
    """

    def __init__(self, client, location, log_class):
        super(Logs, self).__init__(client, location, 'logs', log_class)


class Log(Resource, Deletable):
    """A log file in a node instance

    :ivar `vas.shared.NodeInstances.NodeInstance`   instance:       The node instance that the log belongs to
    :ivar `datetime.datetime`                       last_modified:  The last modified stamp of the log
    :ivar str                                       name:           The name of the log
    :ivar `vas.shared.Security.Security`            security:       The resource's security
    :ivar int                                       size:           The size of the log
    """

    @property
    def instance(self):
        self.__instance = self.__instance or self.__instance_class(self._client, self.__instance_location)
        return self.__instance

    @property
    def last_modified(self):
        return self.__last_modified

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    def __init__(self, client, location, instance_type, instance_class):
        super(Log, self).__init__(client, location)

        self.__content_location = LinkUtils.get_link_href(self._details, 'content')
        self.__instance_location = LinkUtils.get_link_href(self._details, instance_type)

        self.__instance_class = instance_class

    def reload(self):
        """Reloads the log's details from the server"""

        super(Log, self).reload()
        self.__last_modified = datetime.utcfromtimestamp(self._details['last-modified'])
        self.__name = self._details['name']
        self.__size = self._details['size']
        self.__instance = None

    def content(self, start_line=None, end_line=None):
        """Get the content of the log

        :param int  start_line: The start point, in lines, of the content to return. A value of :obj:`None` will result
                                in content from the start of the file being returned. If the provided value is greater
                                than the number of lines in the file, the returned content will be empty.
        :param int  end_line:   The end point, in lines, of the content to return. A value of :obj:`None` will result in
                                content up to the end of the file being returned. If the provided value is greater than
                                the number of lines in the file, content up to and including the last line in the file
                                will be returned.
        :rtype:     :obj:`str`
        :return:    The root directory of the extracted agent
        """

        url = self.__content_location

        if start_line or end_line:
            url += '?'

        if start_line:
            url += "start-line={}".format(start_line)

        if start_line and end_line:
            url += '&'

        if end_line:
            url += "end-line={}".format(end_line)

        return self._client.get(url)
