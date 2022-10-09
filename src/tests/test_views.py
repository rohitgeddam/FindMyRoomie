from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.response = self.client.login(username="admin", password="admin")

    def test_home(self):
        self.client = Client()
        response = self.client.get(reverse("home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_profile(self):
        self.client = Client()
        self.response = self.client.get(reverse("profile"))

        self.assertTrue(200, self.response.status_code)

    def test_profile_edit_get(self):
        self.client = Client()
        self.response = self.client.get(reverse("profile_edit"))

        self.assertTrue(200, self.response.status_code)

    def test_profile_edit_post(self):
        self.client = Client()
        self.response = self.client.post(reverse("profile_edit"))

        self.assertEquals(self.response.status_code, 302)

    def test_findpeople(self):
        self.client = Client()
        self.response = self.client.get(reverse("findpeople"))

        self.assertTrue(200, self.response.status_code)

    def test_myroom(self):
        self.client = Client()
        self.response = self.client.get(reverse("myroom"))

        self.assertTrue(200, self.response.status_code)

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
