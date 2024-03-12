from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen_service.models import Dish, DishType


class ModelTest(TestCase):

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="TestType",
            description="TestDescription",
            country="TestCountry"
        )
        dish = Dish.objects.create(
            name="TestName",
            description="TestDescription",
            price=2,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), dish.name)

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="TestType",
            description="TestDescription",
            country="TestCountry"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="TestUsername",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="TestPassword123",
            years_of_experience=3
        )
        self.assertEqual(
            str(cook), f"{cook.first_name} {cook.last_name}"
        )

    def test_create_cook(self):
        username = "TestUsername"
        first_name = "TestFirstName"
        last_name = "TestLastName"
        password = "TestPassword123"
        years_of_experience = 3

        cook = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.first_name, first_name)
        self.assertEqual(cook.last_name, last_name)
        self.assertEqual(
            cook.years_of_experience, years_of_experience
        )
        self.assertTrue(
            cook.check_password(password)
        )
