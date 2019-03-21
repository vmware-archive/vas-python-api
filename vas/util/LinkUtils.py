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


from vas.VFabricAdministrationServerError import VFabricAdministrationServerError

class LinkUtils:
    @classmethod
    def get_link_hrefs(cls, json, rel):
        return [link['href'] for link in json['links'] if link['rel'] == rel]

    @classmethod
    def get_link_href(cls, json, rel):
        hrefs = cls.get_link_hrefs(json, rel)
        if len(hrefs) == 1:
            return hrefs[0]
        else:
            raise VFabricAdministrationServerError("There are {} links for rel '{}'".format(len(hrefs), rel))

    @classmethod
    def get_self_link_href(cls, json):
        return cls.get_link_href(json, 'self')


    def __repr__(self):
        return "{}()".format(self.__class__.__name__)
