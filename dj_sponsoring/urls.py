# coding=utf-8

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'dj-sponsoring'
urlpatterns = [
    path(
        route="sponsors/create/",
        view=views.SponsorCreateView.as_view(),
        name='sponsor-create',
    ),
    path(
        route="sponsors/<int:pk>/delete/",
        view=views.SponsorDeleteView.as_view(),
        name='sponsor-delete',
    ),
    path(
        route="sponsors/<int:pk>/",
        view=views.SponsorDetailView.as_view(),
        name='sponsor-detail',
    ),
    path(
        route="sponsors/<int:pk>/update/",
        view=views.SponsorUpdateView.as_view(),
        name='sponsor-update',
    ),
    path(
        route="sponsors/",
        view=views.SponsorListView.as_view(),
        name='sponsor-list',
    ),
    path(
        route="sponsors/image/create/",
        view=views.SponsorImageCreateView.as_view(),
        name='sponsor-image-create',
    ),
    path(
        route="sponsors/image/<int:pk>/delete/",
        view=views.SponsorImageDeleteView.as_view(),
        name='sponsor-image-delete',
    ),
    path(
        route="sponsors/image/<int:pk>/",
        view=views.SponsorImageDetailView.as_view(),
        name='sponsor-image-detail',
    ),
    path(
        route="sponsors/image/<int:pk>/update/",
        view=views.SponsorImageUpdateView.as_view(),
        name='sponsor-image-update',
    ),
    path(
        route="sponsors/image/",
        view=views.SponsorImageListView.as_view(),
        name='sponsor-image-list',
    ),
    path(
        route="sponsors/file/create/",
        view=views.SponsorFileCreateView.as_view(),
        name='sponsor-file-create',
    ),
    path(
        route="sponsors/file/<int:pk>/delete/",
        view=views.SponsorFileDeleteView.as_view(),
        name='sponsor-file-delete',
    ),
    path(
        route="sponsors/file/<int:pk>/",
        view=views.SponsorFileDetailView.as_view(),
        name='sponsor-file-detail',
    ),
    path(
        route="sponsors/file/<int:pk>/update/",
        view=views.SponsorFileUpdateView.as_view(),
        name='sponsor-file-update',
    ),
    path(
        route="sponsors/file/",
        view=views.SponsorFileListView.as_view(),
        name='sponsor-file-list',
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)