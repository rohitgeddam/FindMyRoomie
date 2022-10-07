from django.test import TestCase, Client
from django.urls import reverse

# from base.views import home, profile, findpeople, myroom
# from unittest.mock import patch

# import json


class TestViews(TestCase):
    def test_home(self):
        client = Client()
        response = client.get(reverse("home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    # def test_profile(self):
    #     client = Client()
    #     response = client.post(reverse("profile"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "pages/profile.html")

    #     with mock.patch('profiles.views.ProfileForm.is_valid') as mock_profile_form:
    #         mock_profile_form.return_value = True
    #         request = self.factory.post(reverse("profile"), data={})
    #         response = profile(request)

    # def test_findpeople(self):
    #     client = Client()
    #     response = client.get(reverse("findpeople"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "pages/findpeople.html")

    # def test_myroom(self):
    #     client = Client()
    #     response = client.get(reverse("myroom"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "pages/myroom.html")

    def test_user_logout(self):
        client = Client()
        response = client.get(reverse("user_logout"))

        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
