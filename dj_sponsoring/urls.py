# coding=utf-8

"""urls for the dj-sponsoring package."""


from django.urls import path

from . import views


app_name = 'dj-sponsoring'
urlpatterns = [
    path(
        route="sponsors",
        view=views.SponsorListView.as_view(),
        name='sponsors-list',
    ),
    path(
        route="sponsors/create",
        view=views.SponsorCreateView.as_view(),
        name='sponsor-create',
    ),
    path(
        route="sponsors/<int:pk>",
        view=views.SponsorDetailView.as_view(),
        name='sponsor-detail',
    ),
    path(
        route="sponsors/<int:pk>/update",
        view=views.SponsorUpdateView.as_view(),
        name='sponsor-update',
    ),
    path(
        route="sponsors/<int:pk>/delete",
        view=views.SponsorDeleteView.as_view(),
        name='sponsor-delete',
    ),
    path(
        route="sponsors/<int:pk>/images",
        view=views.SponsorImageListView.as_view(),
        name='sponsor-list-images',
    ),
    path(
        route="sponsors/<int:pk>/images/create",
        view=views.SponsorImageCreateView.as_view(),
        name='sponsor-create-image',
    ),
    path(
        route="sponsors/<int:pk>/documents",
        view=views.SponsorDocumentListView.as_view(),
        name='sponsor-list-document',
    ),
    path(
        route="sponsors/<int:pk>/documents/create",
        view=views.SponsorDocumentCreateView.as_view(),
        name='sponsor-create-document',
    ),
    path(
        route="sponsors/images/<int:pk>",
        view=views.SponsorImageDetailView.as_view(),
        name='sponsors-images-detail',
    ),
    path(
        route="sponsors/images/<int:pk>/update",
        view=views.SponsorImageUpdateView.as_view(),
        name='sponsors-images-update',
    ),
    path(
        route="sponsors/images/<int:pk>/delete",
        view=views.SponsorImageDeleteView.as_view(),
        name='sponsors-images-delete',
    ),
    path(
        route="sponsors/documents/<int:pk>",
        view=views.SponsorDocumentDetailView.as_view(),
        name='sponsors-documents-detail',
    ),
    path(
        route="sponsors/documents/<int:pk>/update",
        view=views.SponsorDocumentUpdateView.as_view(),
        name='sponsors-documents-update',
    ),
    path(
        route="sponsors/documents/<int:pk>/delete",
        view=views.SponsorDocumentDeleteView.as_view(),
        name='sponsors-documents-delete',
    ),
]
