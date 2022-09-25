from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            messages.success(
                request, 'Thank you for your message.\
                     We will contact you soon.'
                )
            try:
                send_mail(
                    subject, message, from_email, ["office@stoicshirts22.com"]
                    )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")

    return render(request, "contact/contact.html", {"form": form})


def successView(request):
    """
    Function to return the success template
    """
    return render(request, 'contact/success/success.html')


def subscribeView(request):
    """
    Function to return the subscribe template
    """
    return render(request, 'contact/subscribe/subscribe.html')
