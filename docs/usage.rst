=====
Usage
=====

To use Django Sponsoring in a project, add it to your `INSTALLED_APPS`:

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
