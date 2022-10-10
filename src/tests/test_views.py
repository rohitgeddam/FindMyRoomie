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
