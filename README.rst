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

With the power of `python-anyconfig <https://github.com/ssato/python-anyconfig>`_,
**moban-anyconfig** allows moban to use more data formats than yaml and json.

Given the following toml file, sample.toml:

.. code-block::

   title = "TOML Example"
   [owner]
   name = "Tom Preston-Werner"


You can do:


.. code-block:: bash

   $ moban -c sample.toml "{{owner.name}} made {{title}}"
   Templating {{owner.na... to moban.output
   Templated 1 file.
   $ cat moban.output
   Tom Preston-Werner made TOML Example

Not limited to toml, you can supply moban with the following data formats:

.. csv-table:: Always supported formats, quoting from python-anyconfig
   :header: "Format", "Type", "Requirement"
   :widths: 15, 10, 40

   JSON, json, ``json`` (standard lib) or ``simplejson``
   Ini-like, ini, ``configparser`` (standard lib)
   Pickle, pickle, ``pickle`` (standard lib)
   XML, xml, ``ElementTree`` (standard lib)
   Java properties, properties, None (native implementation with standard lib)
   B-sh, shellvars, None (native implementation with standard lib)

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

**Why not to use python-anyconfig itself, but yet another package?**

moban-anyconfig gives you a promise of any location which `python-anyconfig` does not support.

**Why do it mean 'any location'?**

Thanks to `pyfilesystem 2 <https://github.com/PyFilesystem/pyfilesystem2>`_,
moban-anyconfig is able to read data back from `git repo <https://github.com/moremoban/gitfs2>`_, `pypi <https://github.com/moremoban/pypifs>`_ package, `http(s) <https://github.com/moremoban/httpfs>`_, zip,
tar, ftp, `s3 <https://github.com/PyFilesystem/s3fs>`_ or `you name it <https://www.pyfilesystem.org/page/index-of-filesystems/>`_.


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
