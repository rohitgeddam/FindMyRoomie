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
from django.test import TestCase
from base.models import Profile
from django.contrib.auth import get_user_model


class TestModels(TestCase):
    def test_user_profile_model(self):
        user = get_user_model().objects.create_user(
            "admin@ncsu.edu", "password"
        )
        profile = Profile.objects.get(user=user)
        profile.name = "Arun"
        profile.bio = "Loving Life"
        profile.birth_date = "2000-11-15"
        profile.hometown = "Chennai"
        profile.gender = "Male"
        profile.degree = "Masters Program (MS)"
        profile.diet = "Non Veg"
        profile.country = "India"
        profile.visibility = "True"
        profile.preference_gender = "Male"
        profile.preference_country = "India"
        profile.preference_degree = "Masters Program (MS)"
        profile.preference_course = "Computer Science"
        profile.preference_diet = "Non Veg"
        profile.is_profile_complete = "True"
        profile.save()
        self.assertEqual(user.email, "admin@ncsu.edu")
        self.assertEqual(profile.name, "Arun")
        self.assertEqual(profile.bio, "Loving Life")
        self.assertEqual(profile.birth_date, "2000-11-15")
        self.assertEqual(profile.hometown, "Chennai")
        self.assertEqual(profile.gender, "Male")
        self.assertEqual(profile.degree, "Masters Program (MS)")
        self.assertEqual(profile.diet, "Non Veg")
        self.assertEqual(profile.country, "India")
        self.assertEqual(profile.visibility, "True")
        self.assertEqual(profile.preference_gender, "Male")
        self.assertEqual(profile.preference_country, "India")
        self.assertEqual(profile.preference_degree, "Masters Program (MS)")
        self.assertEqual(profile.preference_course, "Computer Science")
        self.assertEqual(profile.preference_diet, "Non Veg")
        self.assertEqual(profile.is_profile_complete, "True")
