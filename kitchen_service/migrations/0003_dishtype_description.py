# Generated by Django 5.0.3 on 2024-03-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen_service", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="dishtype",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
