# Generated by Django 4.2.1 on 2023-06-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_productmodel_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermodel",
            name="transaction_id",
            field=models.CharField(max_length=5, null=True),
        ),
    ]
