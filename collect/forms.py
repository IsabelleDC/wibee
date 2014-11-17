from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from collect.models import Place, User


class EmailUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):

        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


# class PlaceForm(ModelForm):
#     # name = forms.CharField()
#     class Meta:
#         model = Place

