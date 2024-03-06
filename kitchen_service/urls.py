from django.urls import path

from kitchen_service.views import (
    index,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDetailView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    CookListView,
    CookDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishs/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/detail/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-type/<int:pk>/create/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),

]


app_name = "kitchen_service"
