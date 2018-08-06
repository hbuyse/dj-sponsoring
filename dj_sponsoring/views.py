# coding=utf-8

"""Views."""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
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
    """View that returns the list of sponsors."""

    model = Sponsor
    paginate_by = 10
    context_object_name = 'sponsors'


class SponsorDetailView(DetailView):
    """Show the details of a sponsor."""

    model = Sponsor


class SponsorCreateView(PermissionRequiredMixin, CreateView):
    """Create a sponsor."""

    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.add_sponsor'

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorUpdateView(PermissionRequiredMixin, UpdateView):
    """Update a sponsor."""

    model = Sponsor
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsor'

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorDeleteView(PermissionRequiredMixin, DeleteView):
    """View that allows the deletion of a sponsor."""

    model = Sponsor
    permission_required = 'dj_sponsoring.delete_sponsor'

    def get_success_url(self, **kwargs):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-list')


class SponsorImageListView(ListView):
    """List the images."""

    model = SponsorImage
    paginate_by = 10
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        """."""
        context = super().get_context_data(**kwargs)
        context['sponsor'] = Sponsor.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self, *args, **kwargs):
        """."""
        qs = SponsorImage.objects.all()
        if 'pk' in self.kwargs:
            qs = SponsorImage.objects.filter(sponsor__id=self.kwargs['pk'])
        return qs


class SponsorImageDetailView(DetailView):
    """Show the detail of an image."""

    model = SponsorImage

    def get_context_data(self, **kwargs):
        """."""
        context = super().get_context_data(**kwargs)
        return context


class SponsorImageCreateView(PermissionRequiredMixin, CreateView):
    """SponsorImageCreateView."""

    model = SponsorImage
    fields = ['alt', 'description', 'img']
    permission_required = 'dj_sponsoring.add_sponsorimage'

    def get_initial(self):
        """."""
        initial = dict()

        if 'pk' in self.kwargs:
            initial['sponsor'] = Sponsor.objects.get(id=self.kwargs['pk'])

        return initial

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-detail-image', kwargs={'pk': self.object.id})


class SponsorImageUpdateView(PermissionRequiredMixin, UpdateView):
    """SponsorImageUpdateView."""

    model = SponsorImage
    fields = '__all__'
    permission_required = 'dj_sponsoring.change_sponsorimage'

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageDeleteView(PermissionRequiredMixin, DeleteView):
    """SponsorImageDeleteView."""

    model = SponsorImage
    permission_required = 'dj_sponsoring.delete_sponsorimage'

    def get_success_url(self):
        """Get the URL after the success."""
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
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentUpdateView(UpdateView):
    """SponsorDocumentUpdateView."""

    model = SponsorDocument
    fields = '__all__'

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-document-detail', kwargs={'pk': self.object.id})


class SponsorDocumentDeleteView(DeleteView):
    """SponsorDocumentDeleteView."""

    model = SponsorDocument

    def get_success_url(self):
        """Get the URL after the success."""
        return reverse('dj-sponsoring:sponsor-document-list')
