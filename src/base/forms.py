from django import forms
from .models import Profile


class PersonForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'bio', 'birth_date', 'hometown')
