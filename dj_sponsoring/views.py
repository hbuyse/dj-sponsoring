# coding=utf-8

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import (
    Sponsor,
    SponsorDocument,
    SponsorImage,
)


class SponsorListView(ListView):
    model = Sponsor
    context_object_name = 'sponsors'


class SponsorDetailView(DetailView):
    model = Sponsor


class SponsorCreateView(PermissionRequiredMixin, CreateView):
    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsor'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsor'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Sponsor
    permission_required = 'dj_sponsoring.delete_sponsor'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-list')


class SponsorImageListView(ListView):
    model = SponsorImage
    context_object_name = 'images'


class SponsorImageDetailView(DetailView):
    model = SponsorImage


class SponsorImageCreateView(PermissionRequiredMixin, CreateView):
    model = SponsorImage
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsorimage'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageUpdateView(PermissionRequiredMixin, UpdateView):
    model = SponsorImage
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsorimage'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = SponsorImage
    permission_required = 'dj_sponsoring.delete_sponsorimage'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-list')


class SponsorDocumentListView(ListView):
    model = SponsorDocument


class SponsorDocumentDetailView(DetailView):
    model = SponsorDocument


class SponsorDocumentCreateView(PermissionRequiredMixin, CreateView):
    model = SponsorDocument
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsordocument'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentUpdateView(PermissionRequiredMixin, UpdateView):
    model = SponsorDocument
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsordocument'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentDeleteView(PermissionRequiredMixin, DeleteView):
    model = SponsorDocument
    permission_required = 'dj_sponsoring.delete_sponsordocument'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-document-list')
