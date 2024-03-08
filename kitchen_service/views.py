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
    paginate_by = 7


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        all_cooks = Cook.objects.all()
        all_dish_types = DishType.objects.all()
        context["all_cooks"] = all_cooks
        context["all_dish_types"] = all_dish_types
        return context


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen_service/dish_form.html"

    def get_success_url(self):
        return reverse_lazy("kitchen_service:dish-detail", kwargs={"pk": self.object.pk})


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    context_object_name = "dish_type_list"
    template_name = "kitchen_service/dish_type_list.html"
    paginate_by = 5


class DishTypeDetailView(generic.DetailView):
    model = DishType
    queryset = DishType.objects.all()
    template_name = "kitchen_service/dish_type_detail.html"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_service/dish_type_form.html"
    success_url = reverse_lazy("kitchen_service:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_service/dish_type_form.html"

    def get_success_url(self):
        return reverse_lazy("kitchen_service:dish-type-detail", kwargs={"pk": self.object.pk})


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen_service:dish-type-list")


class CookListView(generic.ListView):
    model = Cook


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_service:cook-list")

