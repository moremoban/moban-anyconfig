================================================================================
moban-anyconfig
================================================================================

.. image:: https://api.travis-ci.org/moremoban/moban-anyconfig.svg
   :target: http://travis-ci.org/moremoban/moban-anyconfig

.. image:: https://codecov.io/github/moremoban/moban-anyconfig/coverage.png
   :target: https://codecov.io/github/moremoban/moban-anyconfig
.. image:: https://badge.fury.io/py/moban-anyconfig.svg
   :target: https://pypi.org/project/moban-anyconfig

.. image:: https://pepy.tech/badge/moban-anyconfig/month
   :target: https://pepy.tech/project/moban-anyconfig/month

.. image:: https://img.shields.io/github/stars/moremoban/moban-anyconfig.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/moban-anyconfig/stargazers

.. image:: https://dev.azure.com/moremoban/moban-anyconfig/_apis/build/status/moremoban.moban-anyconfig?branchName=master
   :target: https://dev.azure.com/moremoban/moban-anyconfig/_build/latest?definitionId=2&branchName=master

It allows moban to use more data formats than yaml and json.

Given the following toml file, sample.toml:

.. code-block::

   title = "TOML Example"
   [owner]
   name = "Tom Preston-Werner"


You can do:


.. code-block:: bash

   $ moban -c sample.toml "{{name}} made {{title}}"
   Templating {{owner.na... to moban.output
   Templated 1 file.
   $ cat moban.output
   Tom Preston-Werner made TOML Example

NOTE
--------

For any of the following data formats, you elect to install by yourself.

.. csv-table:: Supported formats by pluggable backend modules
   :header: "Format", "Type", "Required backend"
   :widths: 15, 10, 40

   Amazon Ion, ion, ``anyconfig-ion-backend`` 
   BSON, bson, ``anyconfig-bson-backend`` 
   CBOR, cbor, ``anyconfig-cbor-backend``  or ``anyconfig-cbor2-backend`` 
   ConifgObj, configobj, ``anyconfig-configobj-backend`` 
   MessagePack, msgpack, ``anyconfig-msgpack-backend``

Or you could choose to install all:

.. code-block:: bash

   $ pip install moban-anyconfig[all-backends]



Installation
================================================================================


You can install moban-anyconfig via pip:

.. code-block:: bash

    $ pip install moban-anyconfig


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/moban-anyconfig.git
    $ cd moban-anyconfig
    $ python setup.py install
