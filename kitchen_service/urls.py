from django.urls import path

from kitchen_service.views import (
    index,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/detail/", DishDetailView.as_view(), name="dish-detail")

]


app_name = "kitchen_service"
