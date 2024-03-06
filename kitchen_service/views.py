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


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    context_object_name = "dish_type_list"
    template_name = "kitchen_service/dish_type_list.html"
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_service/dish_type_form.html"
    success_url = reverse_lazy("kitchen_service:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen_service:dish-type-list")


class CookListView(generic.ListView):
    model = Cook


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_service:cook-list")

