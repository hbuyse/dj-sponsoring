# coding=utf-8

from django.contrib.auth.decorators import permission_required
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
        name='sponsors-create',
    ),
    path(
        route="sponsors/<int:pk>",
        view=views.SponsorDetailView.as_view(),
        name='sponsors-detail',
    ),
    path(
        route="sponsors/<int:pk>/update",
        view=views.SponsorUpdateView.as_view(),
        name='sponsors-update',
    ),
    path(
        route="sponsors/<int:pk>/delete",
        view=views.SponsorDeleteView.as_view(),
        name='sponsors-delete',
    ),
    path(
        route="sponsors/<int:pk>/images",
        view=views.SponsorImageListView.as_view(),
        name='sponsors-delete',
    ),
    path(
        route="sponsors/<int:pk>/images/create",
        view=views.SponsorImageCreateView.as_view(),
        name='sponsors-delete',
    ),
    path(
        route="sponsors/images/create",
        view=views.SponsorImageCreateView.as_view(),
        name='sponsors-images-create',
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
        route="sponsors/documents",
        view=views.SponsorDocumentListView.as_view(),
        name='sponsors-documents-list',
    ),
    path(
        route="sponsors/documents/create",
        view=views.SponsorDocumentCreateView.as_view(),
        name='sponsors-documents-create',
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
