=====
Usage
=====

To use Django Sponsoring in a project, add it to your `INSTALLED_APPS`:

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
