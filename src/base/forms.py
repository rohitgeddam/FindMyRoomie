from django import forms
from .models import Profile
 
 
class ProfileForm(forms.ModelForm):
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