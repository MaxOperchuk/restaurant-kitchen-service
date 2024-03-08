from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_service.models import Dish, DishType

DISH_LIST_URL = reverse("kitchen_service:dish-list")
DISH_CREATION_URL = reverse("kitchen_service:dish-create")
DISH_TYPE_LIST_URL = reverse("kitchen_service:dish-type-list")
DISH_TYPE_CREATION_URL = reverse("kitchen_service:dish-type-create")
COOK_LIST_URL = reverse("kitchen_service:cook-list")
LOGIN_URL = reverse("login")


class UnregisteredUserTest(TestCase):
    def test_login_required_dish_list_page(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_dish_creation_page(self):
        response = self.client.get(DISH_CREATION_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_dish_type_list_page(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_dish_type_creation_page(self):
        response = self.client.get(DISH_TYPE_CREATION_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_cook_list_page(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_can_det_to_login_pade(self):
        response = self.client.get(LOGIN_URL)
        self.assertEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUsername",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="TestPassword123",
            years_of_experience=3
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(
            name="TestType",
            description="TestDescription",
            country="TestCountry"
        )

    def test_retrieve_dishes(self):

        Dish.objects.create(
            name="TestName",
            description="TestDescription",
            price=2,
            dish_type=self.dish_type
        )

        Dish.objects.create(
            name="TestName_2",
            description="TestDescription_2",
            price=2,
            dish_type=self.dish_type
        )

        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(
            response,
            "kitchen_service/dish_list.html"
        )

    def test_retrieve_dish_detail(self):
        test_dish = Dish.objects.create(
            id=1,
            name="TestName",
            description="TestDescription",
            price=2,
            dish_type=self.dish_type
        )

        response = self.client.get(
            reverse(
                "kitchen_service:dish-detail",
                kwargs={"pk": test_dish.pk}
            )
        )

        response_object = response.context_data["object"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_dish, response_object)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUsername",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="TestPassword123",
            years_of_experience=3
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(
            name="TestType1",
            description="TestDescription1",
            country="TestCountry1"
        )

        DishType.objects.create(
            name="TestType2",
            description="TestDescription2",
            country="TestCountry2"
        )

        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )

        self.assertTemplateUsed(
            response,
            "kitchen_service/dish_type_list.html"
        )

    def test_retrieve_dish_type_detail(self):
        test_dish_type = DishType.objects.create(
            id=1,
            name="TestType1",
            description="TestDescription1",
            country="TestCountry1"
        )

        response = self.client.get(
            reverse(
                "kitchen_service:dish-type-detail",
                kwargs={"pk": test_dish_type.pk}
            )
        )

        response_object = response.context_data["object"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_dish_type, response_object)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUsername",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="TestPassword123",
            years_of_experience=3
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        cooks = get_user_model().objects.all()

        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )

        self.assertTemplateUsed(
            response,
            "kitchen_service/cook_list.html"
        )
