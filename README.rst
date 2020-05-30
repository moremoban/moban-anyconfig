================================================================================
moban-anyconfig
================================================================================

.. image:: https://api.travis-ci.org/moremoban/moban-anyconfig.svg
   :target: http://travis-ci.org/moremoban/moban-anyconfig

.. image:: https://codecov.io/github/moremoban/moban-anyconfig/coverage.png
   :target: https://codecov.io/github/moremoban/moban-anyconfig
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

   $ moban -c sample.toml "moban-anyconfig mae "



Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/moban-anyconfig.git
    $ cd moban-anyconfig
    $ python setup.py install
