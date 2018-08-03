# coding=utf-8

"""Views."""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin

from .models import (
    Sponsor,
    SponsorDocument,
    SponsorImage,
)


class SponsorListView(ListView):
    """SponsorListView."""

    model = Sponsor
    context_object_name = 'sponsors'


class SponsorDetailView(DetailView):
    """SponsorDetailView."""

    model = Sponsor


class SponsorCreateView(PermissionRequiredMixin, CreateView):
    """SponsorCreateView."""

    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsor'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorUpdateView(PermissionRequiredMixin, UpdateView):
    """SponsorUpdateView."""

    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsor'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorDeleteView(PermissionRequiredMixin, DeleteView):
    """SponsorDeleteView."""

    model = Sponsor
    permission_required = 'dj_sponsoring.delete_sponsor'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-list')


class SponsorImageListView(SingleObjectMixin, ListView):
    """SponsorImageListView."""

    paginate_by = 10
    template_name = "dj_sponsoring/sponsor_list_images.html"

    def get(self, request, *args, **kwargs):
        """."""
        self.object = self.get_object(queryset=Sponsor.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """."""
        context = super().get_context_data(**kwargs)
        context['sponsor'] = self.object
        return context

    def get_queryset(self):
        """."""
        return self.object.sponsorimage_set.all()


class SponsorImageDetailView(DetailView):
    """SponsorImageDetailView."""

    model = SponsorImage


class SponsorImageCreateView(PermissionRequiredMixin, CreateView):
    """SponsorImageCreateView."""

    model = SponsorImage
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsorimage'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageUpdateView(PermissionRequiredMixin, UpdateView):
    """SponsorImageUpdateView."""

    model = SponsorImage
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsorimage'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageDeleteView(PermissionRequiredMixin, DeleteView):
    """SponsorImageDeleteView."""

    model = SponsorImage
    permission_required = 'dj_sponsoring.delete_sponsorimage'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-image-list')


class SponsorDocumentListView(ListView):
    """SponsorDocumentListView."""

    model = SponsorDocument


class SponsorDocumentDetailView(DetailView):
    """SponsorDocumentDetailView."""

    model = SponsorDocument


class SponsorDocumentCreateView(CreateView):
    """SponsorDocumentCreateView."""

    model = SponsorDocument
    fields = '__all__'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentUpdateView(UpdateView):
    """SponsorDocumentUpdateView."""

    model = SponsorDocument
    fields = '__all__'

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentDeleteView(DeleteView):
    """SponsorDocumentDeleteView."""

    model = SponsorDocument

    def get_success_url(self):
        """."""
        return reverse('dj-sponsoring:sponsor-document-list')
