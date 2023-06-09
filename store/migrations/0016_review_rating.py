# Generated by Django 4.2.1 on 2023-06-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0015_alter_review_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.CharField(
                choices=[
                    ("star0", "Zero stelle"),
                    ("star1", "Una stella"),
                    ("star2", "Due stelle"),
                    ("star3", "Tre stelle"),
                    ("star4", "Quattro stelle"),
                    ("star5", "Cinque stelle"),
                ],
                default="star0",
                max_length=20,
            ),
        ),
    ]
