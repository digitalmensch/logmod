logmod
======

Log all calls to a module 

Features
--------

- Log all calls to a module

Example
-------

.. code:: python

    >>> from logmod import logmod
    >>> import secrets
    >>> logmod(secrets)
    >>>
    >>> secret.token_hex(5)
    logmod: call to secret.token_hex with (5,) {}
    'd34eb399f8'
