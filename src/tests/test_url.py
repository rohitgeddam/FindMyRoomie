from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from base.views import home, profile, findpeople, myroom
import json

class TestUrls(SimpleTestCase):
    def test_url(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_profile_url(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func,profile)
    def test_findpeople_url(self):
        url=reverse('findpeople')
        self.assertEquals(resolve(url).func,findpeople)    
    def test_myroom_url(self):
        url=reverse('myroom')
        self.assertEquals(resolve(url).func,myroom)
        
class TestViews(TestCase):
    def test_home(self):
        client = Client()
        response = client.get(reverse("home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_profile(self):
        client = Client()
        response = client.get(reverse("profile"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/profile.html")

    def test_findpeople(self):
        client = Client()
        response = client.get(reverse("findpeople"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/findpeople.html")

    def test_myroom(self):
        client = Client()
        response = client.get(reverse("myroom"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/myroom.html")

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
