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
    DishTypeDetailView,
    DishTypeUpdateView,
    CookListView,
    CookDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/detail/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
         ),
    path(
        "dish-types/<int:pk>/create/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path(
        "dish-types/<int:pk>/deatail/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
         ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),

]


app_name = "kitchen_service"
