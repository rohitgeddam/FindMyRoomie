import factory
import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save

from base.models import Profile


from faker import Faker as RealFaker

real_faker = RealFaker()


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda a: f"{real_faker.name()}@ncsu.edu")

    is_staff = False


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    name = factory.Faker("name")
    bio = factory.Faker("text")
    birth_date = factory.Faker("date")
    hometown = factory.Faker("city")
    country = factory.Faker("country_code")
    preference_country = factory.Faker("country_code")


class Command(BaseCommand):
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
            except BaseException:
                self.stdout.write(self.style.ERROR("Something went wrong!"))
                count -= 1

        self.stdout.write(self.style.SUCCESS(f"Created {count} User(s)"))
