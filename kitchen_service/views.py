from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen_service.models import Dish, DishType, Cook


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        dishes_count = Dish.objects.count()
        dish_types_count = DishType.objects.count()
        cooks_count = Cook.objects.count()

        context = {
            "dishes_count": dishes_count,
            "dish_types_count": dish_types_count,
            "cooks_count": cooks_count
        }
        return render(
            request, "kitchen_service/index.html", context=context
        )


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")