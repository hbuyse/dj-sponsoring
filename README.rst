=============================
Django Sponsoring
=============================

.. image:: https://badge.fury.io/py/dj-sponsoring.svg
    :target: https://badge.fury.io/py/dj-sponsoring

.. image:: https://travis-ci.org/hbuyse/dj-sponsoring.svg?branch=master
    :target: https://travis-ci.org/hbuyse/dj-sponsoring

.. image:: https://codecov.io/gh/hbuyse/dj-sponsoring/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hbuyse/dj-sponsoring

Sponsors pages for django

Documentation
-------------

The full documentation is at https://dj-sponsoring.readthedocs.io.

Quickstart
----------

Install Django Sponsoring::

    pip install dj-sponsoring

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_sponsoring.apps.DjangoSponsoringConfig',
        ...
    )

Add Django Sponsoring's URL patterns:

.. code-block:: python

    from dj_sponsoring import urls as dj_sponsoring_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_sponsoring_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
