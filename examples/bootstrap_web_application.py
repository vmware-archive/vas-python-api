#!/usr/bin/env python3

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
from vas.VFabricAdministrationServer import VFabricAdministrationServer

def __get_parser():
    parser = argparse.ArgumentParser(description='Provision a tc Server and a deploy a web application')

    parser.add_argument('--installation-image', required=True, help='The location of the tc Server installation image')
    parser.add_argument('--revision-image', required=True, help='The location of the web application revision image')
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

for revision_image in tc_server.revision_images:
    print('  Cleaning up old revision image')
    tc_server.revision_images.delete(revision_image)

for installation_image in tc_server.installation_images:
    print('  Cleaning up old installation image')
    tc_server.installation_images.delete(installation_image)

print('Creating installation image')
installation_image = tc_server.installation_images.create('2.7.0.RELEASE', args.installation_image)

print('Creating revision image')
revision_image = tc_server.revision_images.create('petcare', '1.0.0.RELEASE', args.revision_image)

print('Creating group')
group = tc_server.groups.create(name='my-group', nodes=tc_server.nodes)
for node in group.nodes:
    print('  Node {} selected'.format(node.ip_addresses))

print('Creating installation')
installation = group.installations.create(installation_image)

print('Creating instance at http://localhost:8080')
instance = group.instances.create(name='my-instance', installation=installation, properties={'base.jmx.port': 6970})

print('Creating application at /petcare')
application = instance.group_applications.create('/petcare', 'localhost', 'PetCare', 'Catalina')

print('Creating revision')
application.group_revisions.create(revision_image)

print('Starting instance')
instance.start()

print()
input('Instance started.  Press any key to cleanup...')
print()

print('Stopping instance')
instance.stop()

print('Deleting group')
tc_server.groups.delete(group)

print('Deleting revision image')
tc_server.revision_images.delete(revision_image)

print('Deleting installation image')
tc_server.installation_images.delete(installation_image)
