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


from vas.tc_server.Applications import Applications
from vas.tc_server.Groups import Group
from vas.tc_server.Installations import Installation
from vas.tc_server.Instances import Instances, Instance
from vas.tc_server.LiveConfigurations import LiveConfigurations
from vas.tc_server.NodeInstances import NodeInstance
from vas.tc_server.PendingConfigurations import PendingConfigurations
from vas.tc_server.Templates import Template
from vas.test.VasTestCase import VasTestCase

class TestInstances(VasTestCase):
    def test_list(self):
        self._assert_collection(Instances(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/'))

    def test_create_no_optionals(self):
        installation_location = 'https://localhost:8443/tc-server/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/tc-server/v1/groups/0/instances/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/2/instances/4/')

        instance = Instances(self._client, location).create(Installation(self._client, installation_location),
            'example')

        self.assertIsInstance(instance, Instance)
        self._assert_post(location, {'name': 'example', 'installation': installation_location}, 'group-instance')

    def test_create_all_optionals(self):
        installation_location = 'https://localhost:8443/tc-server/v1/groups/2/installations/3/'
        location = 'https://localhost:8443/tc-server/v1/groups/0/instances/'
        self._return_location('https://localhost:8443/tc-server/v1/groups/2/instances/4/')

        instance = Instances(self._client, location).create(Installation(self._client, installation_location),
            'example', layout='SEPARATE', properties={'a': 'alpha', 'b': 'bravo'}, runtime_version='7.0.21.A.RELEASE',
            templates=[
                Template(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'),
                Template(self._client, 'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/')])

        self.assertIsInstance(instance, Instance)
        self._assert_post(location, {'name': 'example', 'installation': installation_location, 'layout': 'SEPARATE',
                                     'properties': {'a': 'alpha', 'b': 'bravo'}, 'runtime-version': '7.0.21.A.RELEASE',
                                     'templates': [
                                         'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/',
                                         'https://localhost:8443/tc-server/v1/groups/1/installations/2/templates/3/'
                                     ]}, 'group-instance')

    def test_detail(self):
        self._assert_item(Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'), [
            ('layout', 'SEPARATE'),
            ('name', 'example'),
            ('runtime_version', '7.0.21.A.RELEASE'),
            ('services', {'Catalina': {'hosts': ['localhost']}}),
            ('state', 'STOPPED'),
            ('group', lambda actual: self.assertIsInstance(actual, Group)),
            ('applications', lambda actual: self.assertIsInstance(actual, Applications)),
            ('installation', lambda actual: self.assertIsInstance(actual, Installation)),
            ('live_configurations', lambda actual: self.assertIsInstance(actual, LiveConfigurations)),
            ('node_instances', [
                NodeInstance(self._client, 'https://localhost:8443/tc-server/v1/nodes/0/instances/5/'),
                NodeInstance(self._client, 'https://localhost:8443/tc-server/v1/nodes/1/instances/6/')
            ]),
            ('pending_configurations', lambda actual: self.assertIsInstance(actual, PendingConfigurations))
        ])

    def test_start_parallel(self):
        Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/').start()
        self._assert_post('https://localhost:8443/tc-server/v1/groups/2/instances/4/state/',
            {'status': 'STARTED', 'serial': False})

    def test_start_serial(self):
        Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/').start(True)
        self._assert_post('https://localhost:8443/tc-server/v1/groups/2/instances/4/state/',
            {'status': 'STARTED', 'serial': True})

    def test_stop_parallel(self):
        Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/').stop()
        self._assert_post('https://localhost:8443/tc-server/v1/groups/2/instances/4/state/',
            {'status': 'STOPPED', 'serial': False})

    def test_stop_serial(self):
        Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/').stop(True)
        self._assert_post('https://localhost:8443/tc-server/v1/groups/2/instances/4/state/',
            {'status': 'STOPPED', 'serial': True})

    def test_update_no_optionals(self):
        installation_location = 'https://localhost:8443/tc-server/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'

        Instance(self._client, location).update(Installation(self._client, installation_location))

        self._assert_post(location, {'installation': installation_location})

    def test_update_all_optionals(self):
        installation_location = 'https://localhost:8443/tc-server/v1/groups/1/installations/2/'
        location = 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'

        Instance(self._client, location).update(Installation(self._client, installation_location), '7.20.27.A.RELEASE')

        self._assert_post(location, {'installation': installation_location, 'runtime-version': '7.20.27.A.RELEASE'})

    def test_delete(self):
        self._assert_deletable(Instance(self._client, 'https://localhost:8443/tc-server/v1/groups/2/instances/4/'))
