# Generated by Django 4.2.11 on 2024-06-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("checked", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("male", "male"),
                            ("female", "female"),
                            ("other", "other"),
                            ("not_specified", "not_specified"),
                        ],
                        default="not_specified",
                        max_length=64,
                        null=True,
                    ),
                ),
                (
                    "comments",
                    models.TextField(
                        blank=True,
                        default="あなたのことをありったけ書いてください！",
                        max_length=1000,
                        null=True,
                    ),
                ),
                ("items", models.IntegerField(blank=True, default=0, null=True)),
                ("age", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "place",
                    models.TextField(
                        blank=True, default="日本", max_length=1000, null=True
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="profile_images/dfl.png",
                        null=True,
                        upload_to="profile_images/",
                    ),
                ),
            ],
        ),
    ]
