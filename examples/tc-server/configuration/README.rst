Web Application
===============

This example illustrates the use of the vFabric Administration Server (VAS) Python API to provision a tc Server installation, and create a tc Server instance that listens on port 8080. The instance is then started at which point the example will wait for ``enter`` to be pressed. Upon ``enter`` being pressed, the instance is stopped and the configuration changed.  The instance is then started at which point the example will wait for ``enter`` to be pressed. Upon ``enter`` being pressed, the instance is stopped and the provisioned environment is cleaned up.

The example creates a group from all of the nodes that are known to the server, i.e. thanks to VAS's group-based administration, the provisioning of the tc Server installation, creation of the instance, and deployment of the web application will occur on every node that's known to the server.

By default, the context path of the web application will be ``/example``, although this can be
customized using the ``--context-path`` option.

Running the example
-------------------

The example requires two arguments:

* The path to the tc Server ZIP file
* The installation image's version

For example::

    ./configuration.py vfabric-tc-server-standard-2.7.0.RELEASE.zip 2.7.0.RELEASE

The example also supports a number of options, allowing you to customize the context path and the details used to connect to the administration server. Use ``--help`` for more details::

    ./configration.py --help
