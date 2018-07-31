# coding=utf-8

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required
from django.urls import path
from . import views


app_name = 'dj-sponsoring'
urlpatterns = [
    path(
        route="sponsors/",
        view=views.SponsorListView.as_view(),
        name='sponsor-list',
    ),
    path(
        route="sponsors/create/",
        view=permission_required('dj_sponsoring.add_sponsor')(views.SponsorCreateView.as_view()),
        name='sponsor-create',
    ),
    path(
        route="sponsors/<int:pk>/",
        view=views.SponsorDetailView.as_view(),
        name='sponsor-detail',
    ),
    path(
        route="sponsors/<int:pk>/delete/",
        view=permission_required('dj_sponsoring.delete_sponsor')(views.SponsorDeleteView.as_view()),
        name='sponsor-delete',
    ),
    path(
        route="sponsors/<int:pk>/update/",
        view=permission_required('dj_sponsoring.change_sponsor')(views.SponsorUpdateView.as_view()),
        name='sponsor-update',
    ),
    path(
        route="sponsors/image/",
        view=views.SponsorImageListView.as_view(),
        name='sponsor-image-list',
    ),
    path(
        route="sponsors/image/create/",
        view=permission_required('dj_sponsoring.add_sponsorimage')(views.SponsorImageCreateView.as_view()),
        name='sponsor-image-create',
    ),
    path(
        route="sponsors/image/<int:pk>/",
        view=views.SponsorImageDetailView.as_view(),
        name='sponsor-image-detail',
    ),
    path(
        route="sponsors/image/<int:pk>/update/",
        view=permission_required('dj_sponsoring.delete_sponsorimage')(views.SponsorImageUpdateView.as_view()),
        name='sponsor-image-update',
    ),
    path(
        route="sponsors/image/<int:pk>/delete/",
        view=permission_required('dj_sponsoring.change_sponsorimage')(views.SponsorImageDeleteView.as_view()),
        name='sponsor-image-delete',
    ),
    path(
        route="sponsors/document/",
        view=views.SponsorDocumentListView.as_view(),
        name='sponsor-document-list',
    ),
    path(
        route="sponsors/document/create/",
        view=permission_required('dj_sponsoring.add_sponsordocument')(views.SponsorDocumentCreateView.as_view()),
        name='sponsor-document-create',
    ),
    path(
        route="sponsors/document/<int:pk>/",
        view=views.SponsorDocumentDetailView.as_view(),
        name='sponsor-document-detail',
    ),
    path(
        route="sponsors/document/<int:pk>/update/",
        view=permission_required('dj_sponsoring.delete_sponsordocument')(views.SponsorDocumentUpdateView.as_view()),
        name='sponsor-document-update',
    ),
    path(
        route="sponsors/document/<int:pk>/delete/",
        view=permission_required('dj_sponsoring.change_sponsordocument')(views.SponsorDocumentDeleteView.as_view()),
        name='sponsor-document-delete',
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
