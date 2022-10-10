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

import factory
import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
from django.db.models.signals import post_save

from base.models import Profile


from faker import Faker as RealFaker

real_faker = RealFaker()


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """Faker Factory for User model"""

    class Meta:
        model = get_user_model()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    # first_name = ""
    # last_name = ""
    email = factory.LazyAttribute(
        lambda a: f"{real_faker.first_name().lower()}@ncsu.edu"
    )

    is_staff = False


class ProfileFactory(factory.django.DjangoModelFactory):
    """Faker Factory for Profile Model"""

    class Meta:
        model = Profile

    # name = factory.Faker("name")
    bio = factory.Faker("text")
    birth_date = factory.Faker("date")
    hometown = factory.Faker("city")
    country = factory.Faker("country_code")
    preference_country = factory.Faker("country_code")


class Command(BaseCommand):
    """Django manage.py command"""

    help = "Seed models using fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs="+", type=int)

    def handle(self, *args, **options):
        try:
            number = options["number"][0]
        except BaseException:
            raise CommandError("Something went wrong!")

        count = number
        for _ in range(number):

            try:
                u = UserFactory()
                p = ProfileFactory(user=u)
                p.name = u.first_name + " " + u.last_name
                p.gender = random.choices(Profile.GENDER_CHOICES)[0][0]
                p.degree = random.choices(Profile.DEGREE_CHOICES)[0][0]
                p.diet = random.choices(Profile.DIET_CHOICES)[0][0]
                p.course = random.choices(Profile.COURSE_CHOICES)[0][0]

                p.preference_gender = random.choices(
                    Profile.PREF_GENDER_CHOICES
                )[0][0]
                p.preference_degree = random.choices(
                    Profile.PREF_DEGREE_CHOICES
                )[0][0]
                p.preference_diet = random.choices(Profile.PREF_DIET_CHOICES)[
                    0
                ][0]
                p.preference_course = random.choices(
                    Profile.PREF_COURSE_CHOICES
                )[0][0]
                p.is_profile_complete = True
                p.save()
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Please make migrations and Migrate. Something went wrong in the DB tables."
                    )
                )
                count = 0
                break
            except BaseException:
                self.stdout.write(self.style.ERROR("Something went wrong!"))
                count -= 1

        self.stdout.write(self.style.SUCCESS(f"Created {count} User(s)"))
