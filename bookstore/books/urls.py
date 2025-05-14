from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("new_books/", views.show_only_new_books, name="new_books"),
    path("sale/", views.on_sale, name="sale"),
    path("search/", views.search, name="search"),
    path("about_book/<str:slug>/", views.about_book, name="about_book"),
]
