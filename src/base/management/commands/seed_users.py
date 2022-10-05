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

    # gender = random.choice(
    #     [Profile.GENDER_MALE, Profile.GENDER_FEMALE, Profile.GENDER_OTHER]
    # )
    # degree = random.choice([Profile.DEGREE_BS, Profile.DEGREE_MS, Profile.DEGREE_PHD])
    # diet = random.choice([Profile.DIET_NON_VEG, Profile.DIET_VEG])
    gender_list = [Profile.GENDER_MALE, Profile.GENDER_FEMALE, Profile.GENDER_OTHER]
    degree_list = [Profile.DEGREE_BS, Profile.DEGREE_MS, Profile.DEGREE_PHD]
    diet_list = [Profile.DIET_NON_VEG, Profile.DIET_VEG]
    
    gender = gender_list[random.randint(0,len(gender_list)-1)]
    degree = degree_list[random.randint(0,len(degree_list)-1)]
    diet = diet_list[random.randint(0,len(diet_list)-1)]
    
    country = factory.Faker("country")


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
            u = UserFactory()
            ProfileFactory(user=u)

        self.stdout.write(self.style.SUCCESS(f"Created {number} User(s)"))
