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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class LinkUtils:
    __KEY_HREF = 'href'

    __KEY_LINKS = 'links'

    __KEY_REL = 'rel'

    __REL_SELF = 'self'

    @classmethod
    def get_collection_self_links(cls, payload, collection_key):
        return [cls.get_link(item, cls.__REL_SELF) for item in payload[collection_key]]

    @classmethod
    def get_link(cls, payload, rel):
        links = cls.get_links(payload, rel)
        if len(links) == 1:
            return links[0]
        else:
            raise VFabricAdministrationServerError("There are {} links for rel '{}'".format(len(links), rel))

    @classmethod
    def get_links(cls, payload, rel=None):
        links = dict()

        for link in payload[cls.__KEY_LINKS]:
            candidate_rel = link[cls.__KEY_REL]
            candidate_href = link[cls.__KEY_HREF]

            values = links.setdefault(candidate_rel, [])
            if candidate_href not in values:
                values.append(candidate_href)

        if rel is None:
            return links
        else:
            return links[rel]

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)
