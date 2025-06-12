from django.urls import path
from . import views

urlpatterns = [
    path("", views.shopping_cart, name="shopping_cart"),
    path("delete_from_cart/<int:pk>/", views.delete_from_shopping_cart, name="delete_from_cart"),
    path("add_to_cart/<int:pk>/", views.add_to_shopping_cart, name="add_to_cart"),
    path("increase_quantity/<int:pk>/", views.increase_quantity, name="increase_quantity"),
    path("decrease_quantity/<int:pk>/", views.decrease_quantity, name="decrease_quantity"),
    path("confirm/", views.confirm_purchase, name="confirm_purchase"),
]
