from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
 
from django_countries.fields import CountryField
 
 
GENDER_CHOICES = (
    ('--', '-----'),
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)
 
DEGREE_CHOICES = (
    ('--', '-----'),
    ("B", "Bachelors Program (BS)"),
    ("M", "Masters Program (MS)"),
    ("P", "Post Docterate (PHD)")
)
 
DIET_CHOICES = (
    ('--', '-----'),
    ("V", "Veg"),
    ("NV", "Non Veg")
)
 
class Profile(models.Model):
    """User Profile Model"""
    name = models.CharField(max_length=100, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hometown = models.CharField(max_length=100, default='')
 
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='--')
    degree = models.CharField(max_length=5, choices=DEGREE_CHOICES, default="--")
    diet = models.CharField(max_length=5, choices=DIET_CHOICES, default="--")
    country = CountryField(blank_label='select country', default="")
 
    def __str__(self):
        return f"{self.user.username}-profile"
 
 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
 
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()