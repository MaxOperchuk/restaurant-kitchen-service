# Generated by Django 5.0.3 on 2024-03-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(null=True),
        ),
    ]
