# Generated by Django 4.2.1 on 2023-05-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_customermodel_productmodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkoutmodel",
            name="name",
            field=models.CharField(default="", max_length=20),
        ),
    ]
