from django.contrib.auth import forms
from django.forms import ModelForm
from collect.models import Place


class PlaceForm(ModelForm):
    # name = forms.CharField()
    class Meta:
        model = Place

