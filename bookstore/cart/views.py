from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import Order, OrderedItem


@login_required
def shopping_cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    items = order.ordereditem_set.all()
    context = {"items": items, "order": order}

    return render(request, "cart/cart.html", context)


@login_required
def add_to_shopping_cart(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        book = Book.objects.get(pk=pk)
        item = order.ordereditem_set.filter(book=book).first()

        if item:
            item.quantity += 1
            item.save()
        else:
            item = OrderedItem(book=book, order=order)
            item.save()

        return redirect("shopping_cart")
    else:
        return redirect("login")


@login_required
def delete_from_shopping_cart(request, pk):
    item = get_object_or_404(OrderedItem, pk=pk)
    item.delete()
    return redirect("shopping_cart")


@login_required
def increase_quantity(request, pk):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    book = Book.objects.get(pk=pk)
    item = order.ordereditem_set.filter(book=book).first()
    if item:
        item.quantity += 1
        item.save()

    updated_data = {
        "total_books_num": order.get_number_of_items,
        "total_price": order.get_price_of_order,
        "quantity": item.quantity,
        "price": item.get_total_price,
    }

    return JsonResponse(updated_data)


@login_required
def decrease_quantity(request, pk):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    book = Book.objects.get(pk=pk)
    item = order.ordereditem_set.filter(book=book).first()
    if item:
        if item.quantity > 1:
            item.quantity -= 1
        else:
            item.quantity = 1
        item.save()

    updated_data = {
        "total_books_num": order.get_number_of_items,
        "total_price": order.get_price_of_order,
        "quantity": item.quantity,
        "price": item.get_total_price,
    }

    return JsonResponse(updated_data)


@login_required
def confirm_purchase(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)

    if request.method == "POST":
        order.phone = request.POST.get("phone-number")
        order.address = request.POST.get("address")
        order.city = request.POST.get("city")
        order.state = request.POST.get("state")
        order.completed = True
        order.save()
        return render(request, "cart/thank_you_page.html")

    items = order.ordereditem_set.all()
    context = {"items": items, "order": order, "customer": customer}

    return render(request, "cart/confirm_purchase.html", context)
