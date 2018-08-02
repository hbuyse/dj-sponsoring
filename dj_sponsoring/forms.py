from django import forms

from .models import Sponsor, SponsorDocument, SponsorImage


class SponsorForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsorImageForm(forms.ModelForm):

    class Meta:
        model = SponsorImage
        fields = '__all__'


class SponsorDocumentForm(forms.ModelForm):

    class Meta:
        model = SponsorDocument
        fields = '__all__'
