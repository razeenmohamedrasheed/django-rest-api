# Generated by Django 4.2.17 on 2024-12-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]