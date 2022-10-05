from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve 
from base.views import home, profile, findpeople, myroom

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
        


