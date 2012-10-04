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

from setuptools import setup, find_packages

setup(
    name='vas',
    version='0.3.0',
    url='http://vfabric.co',
    author='VMware',
    author_email='support@vmware.com',
    description='vFabric Administration Server Python API',
    long_description='A Python API for VMware vFabric Administration Server',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration'
    ],
    packages=find_packages(exclude=["*.test"]),
    install_requires=['requests'],
    test_suite='vas',
    tests_require=['mock']
)
