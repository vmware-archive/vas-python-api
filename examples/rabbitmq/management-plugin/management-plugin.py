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


from __future__ import print_function
import argparse
from vas.VFabricAdministrationServer import VFabricAdministrationServer

def __get_parser():
    parser = argparse.ArgumentParser(description='Provision a tc Server and modify its configuration')

    parser.add_argument('installation_image', help='The path to the installation image')
    parser.add_argument('installation_image_version', help="The installation image's version")
    parser.add_argument('--host', default='localhost',
        help='The vFabric Administration Server host (default: localhost)')
    parser.add_argument('--port', default=8443, type=int, help='The vFabric Administration Server port (default: 8443)')
    parser.add_argument('--username', default='admin',
        help='The vFabric Administration Server username (default: admin)')
    parser.add_argument('--password', default='vmware',
        help='The vFabric Administration Server password (default: password)')

    return parser

args = __get_parser().parse_args()

try:
    rabbitmq = VFabricAdministrationServer(args.host, args.port, args.username, args.password).rabbitmq

    print('Creating installation image... ', end='')
    installation_image = rabbitmq.installation_images.create(args.installation_image_version, args.installation_image)
    print('done')

    print('Creating group... ', end='')
    group = rabbitmq.groups.create('example', rabbitmq.nodes)
    print('done')

    print('Creating installation... ', end='')
    installation = group.installations.create(installation_image)
    print('done')

    print('Creating instance... ', end='')
    instance = group.instances.create('example', installation)
    print('done')

    for plugin in instance.plugins:
        if 'rabbitmq_management' == plugin.name:
            plugin.enable()

    print('Starting instance... ', end='')
    instance.start()
    print('done')

    raw_input('Press any key to cleanup')
finally:
    variables = dir()

    if 'instance' in variables:
        print('Stopping instance... ', end='')
        instance.stop()
        print('done')

    if 'group' in variables:
        print('Deleting group... ', end='')
        rabbitmq.groups.delete(group)
        print('done')

    if 'installation_image' in variables:
        print('Deleting installation image... ', end='')
        rabbitmq.installation_images.delete(installation_image)
        print('done')
