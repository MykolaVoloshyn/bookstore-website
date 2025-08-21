from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib.auth import authenticate, login
from .models import Customer


def signup(request):
    form = CustomerForm()

    if request.method == "POST":
        print("1")
        form = CustomerForm(request.POST)
        print("2")

        if form.is_valid():
            user = form.save()
            print("3")

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            print(5)
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
            print("4")
            login(request, user)
            return redirect("main_page")
        else:
            print("form is not valid")

    return render(request, "customers/sign_up.html", {"form": form})
