vFabric Administration Server Python API
========================================

The vFabric Administration Server (VAS) API is a Python library used for interacting with the `vFabric Administration Server`_.

VAS's primary mode of interaction is via RESTful interface.  This API enables the use of VAS using rich Python types, eliminating the need for a detailed understanding of the REST API and its JSON payloads.

The VAS Python API is licensed under the `Apache Licence, Version 2.0`_.

.. _vFabric Administration Server: http://www.vmware.com/support/pubs/vfabric-vas.html
.. _Apache Licence, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0.html

Installing
----------

The VAS Python API can be installed by running ``pip install vas``.

Dependencies
------------

The VAS Python API requires **Python3**.  This can be installed with the default package manager on most operating systems, or downloaded from the `Python website`_.

Runtime Dependencies
~~~~~~~~~~~~~~~~~~~~

* requests_ (0.13.6)

Development Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

* coverage_ (3.5.2)
* mock_ (1.0b1)
* sphinx_ (1.1.3)

All of these dependencies can be installed by running ``pip install <dependency>``.

.. _Python website: http://python.org/download/
.. _Requests: http://docs.python-requests.org
.. _Coverage: http://nedbatchelder.com/code/coverage/
.. _Mock: http://www.voidspace.org.uk/python/mock/
.. _Sphinx: http://sphinx.pocoo.org
