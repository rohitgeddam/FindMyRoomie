# Generated by Django 4.1.1 on 2022-10-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "base",
            "0006_profile_preference_country_profile_preference_degree_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="preference_gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                max_length=5,
            ),
        ),
    ]
