import factory
import random
from urllib.parse import uses_fragment
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from base.models import Profile

@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("name")

    is_staff = False


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    name = factory.Faker("name")
    bio = factory.Faker("text")
    birth_date = factory.Faker("date")
    hometown = factory.Faker("city")  
    country = factory.Faker("country_code")


class Command(BaseCommand):
    help = "Seed models using fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs="+", type=int)

    def handle(self, *args, **options):
        try:
            number = options["number"][0]
        except:
            raise CommandError("Something went wrong!")

        for _ in range(number):
            
            try:
                u = UserFactory()
                p = ProfileFactory(user=u)
                p.gender = random.choices([Profile.GENDER_MALE, Profile.GENDER_FEMALE, Profile.GENDER_OTHER] * 1000)[0]
                p.degree = random.choices([Profile.DEGREE_BS, Profile.DEGREE_MS, Profile.DEGREE_PHD] * 1000)[0]
                p.diet = random.choices([Profile.DIET_NON_VEG, Profile.DIET_VEG] * 1000)[0]
                p.save()
                print(p.gender, p.degree, p.diet, p.country)
            except: 
                self.stdout.write(self.style.ERROR(f"Something went wrong!"))


        self.stdout.write(self.style.SUCCESS(f"Created {number} User(s)"))
