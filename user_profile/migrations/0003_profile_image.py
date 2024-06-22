# Generated by Django 4.2.11 on 2024-06-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_alter_profile_comments_alter_profile_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_images/dfl.png",
                null=True,
                upload_to="profile_images/",
            ),
        ),
    ]
