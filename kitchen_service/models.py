from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(
        max_length=255,
    )


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)