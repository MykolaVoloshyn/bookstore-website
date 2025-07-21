from django.shortcuts import redirect, render
from contact_us.models import ContactInfo
from contact_us.forms import ContactUsForm


def contact_us(request):
    contact_info = ContactInfo.objects.all().first()
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("contact_us")

    return render(request, "contact_page/contact_us.html", {"contact_info": contact_info})
