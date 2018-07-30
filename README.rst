=============================
Django Sponsoring
=============================

.. image:: https://badge.fury.io/py/django-sponsoring.svg
    :target: https://badge.fury.io/py/django-sponsoring

.. image:: https://travis-ci.org/hbuyse/django-sponsoring.svg?branch=master
    :target: https://travis-ci.org/hbuyse/django-sponsoring

.. image:: https://codecov.io/gh/hbuyse/django-sponsoring/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hbuyse/django-sponsoring

Sponsors pages for django

Documentation
-------------

The full documentation is at https://django-sponsoring.readthedocs.io.

Quickstart
----------

Install Django Sponsoring::

    pip install django-sponsoring

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_sponsoring.apps.DjangoSponsoringConfig',
        ...
    )

Add Django Sponsoring's URL patterns:

.. code-block:: python

    from django_sponsoring import urls as django_sponsoring_urls


    urlpatterns = [
        ...
        url(r'^', include(django_sponsoring_urls)),
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
