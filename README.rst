vas-python-api is no longer actively maintained by VMware, Inc.
===============================================================

vFabric Administration Server Python API
========================================
The vFabric Administration Server (VAS) API is a Python library used for interacting with the `vFabric Administration Server <https://www.vmware.com/support/pubs/vfabric-vas.html>`_.

VAS's primary mode of interaction is via RESTful interface.  This API enables the use of VAS using rich Python types, eliminating the need for a detailed understanding of the REST API and its JSON payloads.


Requirements
------------
The VAS Python API requires Python 2.7.  It has been built and tested on 2.7.3.


Installation
------------
The VAS Python egg is available on `PyPI <https://pypi.python.org/pypi/vas>`_.  To install it run::

    pip install vas


Getting Started
---------------
Examples
~~~~~~~~

A number of `examples <https://github.com/vFabric/vas-python-api/tree/master/examples>`_ are provided:


tc Server
+++++++++
* `Provision tc Server and deploy a web application <https://github.com/vFabric/vas-python-api/tree/master/examples/tc-server/web-application>`_


RabbitMQ
++++++++
* `Provision Rabbit and enable the management plugin <https://github.com/vFabric/vas-python-api/tree/master/examples/rabbitmq/management-plugin>`_


VAS
+++
* `Download, install, and start the VAS agent <https://github.com/vFabric/vas-python-api/tree/master/examples/rabbitmq/management-plugin>`_


Documentation
~~~~~~~~~~~~~
You may also like to look at the `API Documentation <https://packages.python.org/vas>`_.


License
-------
The VAS Python API is licensed under the `Apache Licence, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0.html>`_.
