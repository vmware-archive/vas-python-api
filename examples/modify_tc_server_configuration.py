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


import argparse
import re
from vas.VFabricAdministrationServer import VFabricAdministrationServer

def __get_parser():
    parser = argparse.ArgumentParser(description='Provision a tc Server and modify its configuration')

    parser.add_argument('--installation-image', required=True, help='The location of the tc Server installation image')
    parser.add_argument('--host', default='localhost',
        help='The vFabric Administration Server host (default: localhost)')
    parser.add_argument('--port', default=8443, type=int, help='The vFabric Administration Server port (default: 8443)')

    return parser

args = __get_parser().parse_args()

print('Creating server connection')
vas = VFabricAdministrationServer(args.host, args.port)
tc_server = vas.tc_server
vfabric = vas.vfabric

for group in tc_server.groups:
    print('  Cleaning up old group')
    for instance in group.instances:
        if instance.state == 'STARTED':
            print('    Stopping instance')
            instance.stop()
    tc_server.groups.delete(group)

for installation_image in tc_server.installation_images:
    print('  Cleaning up old installation image')
    tc_server.installation_images.delete(installation_image)

print('Creating installation image')
installation_image = tc_server.installation_images.create('2.7.0.RELEASE', args.installation_image)

print('Creating group')
group = tc_server.groups.create(name='my-group', nodes=tc_server.nodes)
for node in group.nodes:
    print('  Node {} selected'.format(node.ip_addresses))

print('Creating installation')
installation = group.installations.create(installation_image)

print('Creating instance at http://localhost:8080')
instance = group.instances.create(name='my-instance', installation=installation, properties={'base.jmx.port': 6970})

print('Starting instance')
instance.start()

print()
input('Instance started.  Press any key to change configuration...')
print()

print('Stopping instance')
instance.stop()

print('Changing instance http port to 8081')
pending_configuration = None
for configuration in instance.pending_configurations:
    if 'conf/catalina.properties' == configuration.path:
        pending_configuration = configuration
        break

pending_configuration.content = re.sub('bio.http.port=8080', 'bio.http.port=8081', pending_configuration.content)

print('Starting instance')
instance.start()

print()
input('Instance started.  Press any key to cleanup...')
print()

print('Stopping instance')
instance.stop()

print('Deleting group')
tc_server.groups.delete(group)

print('Deleting installation image')
tc_server.installation_images.delete(installation_image)
