# Generated by Django 4.1.7 on 2023-04-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog",
            name="image",
            field=models.FileField(upload_to="dogs/"),
        ),
    ]