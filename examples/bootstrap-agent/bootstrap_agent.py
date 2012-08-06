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
import os
from subprocess import call
from vas.VFabricAdministrationServer import VFabricAdministrationServer


def __get_parser():
    parser = argparse.ArgumentParser(description='Download and start the vFabric Administration Agent')

    parser.add_argument('--host', default='localhost',
        help='The vFabric Administration Server host (default: localhost)')
    parser.add_argument('--port', default=8443, type=int, help='The vFabric Administration Server port (default: 8443)')
    parser.add_argument('--username', default='admin',
        help='The vFabric Administration Server username (default: admin)')
    parser.add_argument('--password', default='vmware',
        help='The vFabric Administration Server password (default: password)')
    parser.add_argument('--location', default=os.curdir,
        help='The location to install the vFabric Administration Agent (default: current working directory)')

    return parser

args = __get_parser().parse_args()

agent_root = VFabricAdministrationServer(args.host, args.port, args.username,
    args.password).vfabric.agent_image.extract_to(args.location)
call(['{}/bin/administration-agent.sh'.format(agent_root), 'start'])
