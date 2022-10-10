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

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, profile, findpeople, myroom, user_logout


class TestUrls(SimpleTestCase):
    def test_url(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_profile_url(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func, profile)

    def test_findpeople_url(self):
        url = reverse("findpeople")
        self.assertEquals(resolve(url).func, findpeople)

    def test_myroom_url(self):
        url = reverse("myroom")
        self.assertEquals(resolve(url).func, myroom)

    def test_logout(self):
        url = reverse("user_logout")
        self.assertEquals(resolve(url).func, user_logout)
