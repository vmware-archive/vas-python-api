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


from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='vas-python-api',
    version='1.0.0.BUILD-SNAPSHOT',
    packages=['vas', 'vas.shared', 'vas.tc_server', 'vas.util', 'vas.vfabric'],
    url='https://github.com/vFabric/vas-python-api',
    author='Ben Hale',
    author_email='bhale@vmware.com',
    description='Python API for accessing the vFabric Administration Server',
    long_description=long_description,
    requires=['requests', 'mock'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration'
    ]
)
