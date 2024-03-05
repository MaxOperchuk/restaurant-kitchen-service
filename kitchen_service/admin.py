from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen_service.models import DishType, Dish, Cook


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(Cook)
class CookAdmin(UserAdmin):
    pass


