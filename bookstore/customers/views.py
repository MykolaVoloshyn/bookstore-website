from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib.auth import authenticate, login
from .models import Customer


def signup(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            customer = Customer.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            customer.save()
            login(request, new_user)
            return redirect("main_page")

    form = CustomerForm()
    return render(request, "customers/sign_up.html", {"form": form})
