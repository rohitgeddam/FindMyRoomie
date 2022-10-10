import django_filters
from base.models import Profile


class ProfileFilter(django_filters.FilterSet):
    """Filter to filter the queryset for profiles"""

    class Meta:
        model = Profile
        fields = ["gender", "degree", "course", "diet", "country"]

        # @property
        # def qs(self):
        #     profiles = super().qs

        #     return profiles.filter(visibility=True)
