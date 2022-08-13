# Generated by Django 4.1 on 2022-08-13 16:55

import datetime
from django.db import migrations, models
import tiny.models.redirect


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Redirect",
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
                ("url", models.URLField()),
                (
                    "shortcode",
                    models.CharField(
                        default=tiny.models.redirect.generate_random_shortcode,
                        max_length=6,
                        unique=True,
                    ),
                ),
                ("created_date", models.DateField(default=datetime.date.today)),
                ("last_accessed_date", models.DateTimeField(null=True)),
                ("redirect_count", models.IntegerField(default=0)),
            ],
        ),
    ]