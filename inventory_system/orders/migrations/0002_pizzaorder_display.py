# Generated by Django 5.0.6 on 2024-09-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pizzaorder",
            name="display",
            field=models.BooleanField(default=True),
        ),
    ]
