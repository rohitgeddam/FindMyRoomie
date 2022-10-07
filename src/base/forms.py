from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if (hasattr(bound_field, "field") and bound_field.name in self.Meta.required_fields):bound_field.field.widget.attrs["required"] = "required"

    class Meta:
        model = Profile
        fields = (
            "name",
            "bio",
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
            "visibility",
            "preference_gender",
            "preference_degree",
            "preference_diet",
            "preference_country",
            "preference_course",
        ]
