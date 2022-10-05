from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
 
from django_countries.fields import CountryField
 
 

 
class Profile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    
    DEGREE_BS = 'B'
    DEGREE_MS = 'M'
    DEGREE_PHD = 'P'
    
    DIET_VEG = 'V'
    DIET_NON_VEG = 'NV'
    
    BLANK = '--'
    
    
    GENDER_CHOICES = (
        (BLANK, '-----'),
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )
    
    DEGREE_CHOICES = (
        (BLANK, '-----'),
        (DEGREE_BS, "Bachelors Program (BS)"),
        (DEGREE_MS, "Masters Program (MS)"),
        (DEGREE_PHD, "Post Docterate (PHD)")
    )
    
    DIET_CHOICES = (
        (BLANK, '-----'),
        (DIET_VEG, "Veg"),
        (DIET_NON_VEG, "Non Veg")
    )

    """User Profile Model"""
    name = models.CharField(max_length=100, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hometown = models.CharField(max_length=100, default='')
 
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default=BLANK)
    degree = models.CharField(max_length=5, choices=DEGREE_CHOICES, default=BLANK)
    diet = models.CharField(max_length=5, choices=DIET_CHOICES, default=BLANK)
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