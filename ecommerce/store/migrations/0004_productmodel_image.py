# Generated by Django 4.2.1 on 2023-05-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_checkoutmodel_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]