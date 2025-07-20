from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:book_pk>/", views.add_comment, name="add_comment"),
    path("delete/", views.delete_comment, name="delete_comment"),
    path("update/", views.update_comment, name="update_comment"),
]
