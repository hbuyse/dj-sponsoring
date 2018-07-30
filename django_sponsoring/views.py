# coding=utf-8

from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from .models import Sponsor, SponsorImage, SponsorFile


class SponsorListView(ListView):
    model = Sponsor
    context_object_name = 'sponsors'


class SponsorDetailView(DetailView):
    model = Sponsor


class SponsorCreateView(CreateView):
    model = Sponsor
    fields = '__all__'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorDeleteView(DeleteView):
    model = Sponsor

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-list')


class SponsorUpdateView(UpdateView):
    model = Sponsor
    fields = '__all__'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-detail', kwargs={'pk': self.object.id})


class SponsorImageCreateView(CreateView):

    model = SponsorImage


class SponsorImageDeleteView(DeleteView):

    model = SponsorImage


class SponsorImageDetailView(DetailView):

    model = SponsorImage


class SponsorImageUpdateView(UpdateView):

    model = SponsorImage


class SponsorImageListView(ListView):

    model = SponsorImage


class SponsorFileCreateView(CreateView):

    model = SponsorFile


class SponsorFileDeleteView(DeleteView):

    model = SponsorFile


class SponsorFileDetailView(DetailView):

    model = SponsorFile


class SponsorFileUpdateView(UpdateView):

    model = SponsorFile


class SponsorFileListView(ListView):

    model = SponsorFile
