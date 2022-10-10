#
# Created on Sun Oct 09 2022
#
# The MIT License (MIT)
# Copyright (c) 2022 Rohit Geddam, Arun Kumar, Teja Varma, Kiron Jayesh, Shandler Mason
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .utils import check_ncsu_email

# from django.contrib.admin.widgets import AdminDateWidget
from .models import Profile


class SignUpForm(UserCreationForm):
    """Build Sign up Form"""

    # username = forms.CharField(label="<b>NCSU</b> E-mail", max_length=100)
    class Meta:
        model = get_user_model()
        fields = [
            "email",
        ]

    def clean(self):
        # data is feteched using the super function of django
        super(SignUpForm, self).clean()

        email = self.cleaned_data.get("email")

        if not check_ncsu_email(email):
            self._errors["email"] = self.error_class(
                ["Please use a valid ncsu email id"]
            )

        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    """Build the User Profile Form"""

    # birth_date = forms.DateField(widget=AdminDateWidget)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if (
                hasattr(bound_field, "field")
                and bound_field.name in self.Meta.required_fields
            ):
                bound_field.field.widget.attrs["required"] = "required"

    class Meta:
        model = Profile
        fields = (
            "name",
            "bio",
            "profile_photo",
            "birth_date",
            "gender",
            "diet",
            "degree",
            "course",
            "hometown",
            "country",
            "visibility",
            "preference_gender",
            "preference_degree",
            "preference_diet",
            "preference_country",
            "preference_course",
        )
        required_fields = [
            "name",
            "bio",
            "birth_date",
            "gender",
            "diet",
            "degree",
            "course",
            "hometown",
            "country",
        ]
        widgets = {
            "birth_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Date",
                    "type": "date",
                },
            )
        }
