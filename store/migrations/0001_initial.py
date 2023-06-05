# Generated by Django 4.2.1 on 2023-05-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CheckOutModel",
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
                ("name", models.CharField(max_length=20)),
                ("surname", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=40)),
                ("city", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=30)),
                ("postalCode", models.IntegerField()),
            ],
        ),
    ]