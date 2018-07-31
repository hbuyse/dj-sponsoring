# coding=utf-8

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


class SponsorImageListView(ListView):
    model = SponsorImage
    context_object_name = 'images'
    queryset = SponsorImage.objects.order_by("sponsor", "created")


class SponsorImageDetailView(DetailView):
    model = SponsorImage


class SponsorImageCreateView(CreateView):
    model = SponsorImage
    fields = '__all__'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorImageDeleteView(DeleteView):
    model = SponsorImage

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-list')


class SponsorImageUpdateView(UpdateView):
    model = SponsorImage
    fields = '__all__'

    def get_success_url(self):
        return reverse('dj-sponsoring:sponsor-image-detail', kwargs={'pk': self.object.id})


class SponsorDocumentCreateView(CreateView):

    model = SponsorDocument


class SponsorDocumentDeleteView(DeleteView):

    model = SponsorDocument


class SponsorDocumentDetailView(DetailView):

    model = SponsorDocument


class SponsorDocumentUpdateView(UpdateView):

    model = SponsorDocument


class SponsorDocumentListView(ListView):

    model = SponsorDocument
