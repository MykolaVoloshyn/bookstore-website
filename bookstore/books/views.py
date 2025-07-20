from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from comments.forms import CommentForm
from .models import Author, Book, Genre, Publisher
from django.core.paginator import Paginator
from django.shortcuts import render


def pagination(request, books, pages=4):
    paginator = Paginator(books, pages)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def main_page(request):
    books = Book.objects.all()
    page_obj = pagination(request, books)
    text = "Book catalog"
    context = {"page_obj": page_obj, "text": text}

    return render(request, "books/main_page.html", context)


def show_only_new_books(request):
    books = Book.objects.filter(new=True)
    page_obj = pagination(request, books)
    text = "New books"
    return render(request, "books/main_page.html", {"page_obj": page_obj, "text": text})


def on_sale(request):
    books = Book.objects.filter(on_sale=True)
    page_obj = pagination(request, books)
    text = "Books on sale"
    return render(request, "books/on_sale.html", {"page_obj": page_obj, "text": text})


def get_genres(request):
    return Genre.objects.all()


def get_authors(request):
    return Author.objects.all()


def get_publishers(request):
    return Publisher.objects.all()


def search(request):
    books = Book.objects.all()
    genres = get_genres(request)
    authors = get_authors(request)
    publishers = get_publishers(request)

    filter_search_name = request.GET.get("search_name", "").lower()

    filter_genres = request.GET.getlist("genre")
    filter_authors = request.GET.getlist("author")
    filter_publishers = request.GET.getlist("publisher")

    if (
        filter_search_name
        or filter_genres
        or filter_authors
        or filter_publishers
        or filter_search_name
    ):
        if filter_search_name:
            books = Book.objects.filter(
                Q(genre__in=filter_genres)
                | Q(author__in=filter_authors)
                | Q(publisher__in=filter_publishers)
                | Q(slug__contains=filter_search_name)
            )
        else:
            books = Book.objects.filter(
                Q(genre__in=filter_genres)
                | Q(author__in=filter_authors)
                | Q(publisher__in=filter_publishers)
            )

    page_obj = pagination(request, books, pages=6)

    context = {
        "books": books,
        "page_obj": page_obj,
        "genres": genres,
        "authors": authors,
        "publishers": publishers,
    }
    return render(request, "books/search.html", context)


def about_book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        form = CommentForm()
        context = {
            "text": "About this book",
            "book": book,
            "form": form,
            "customer": customer,
        }
        return render(request, "books/about_book.html", context)

    return render(request, "books/about_book.html", {"book": book, "text": "About this book"})
