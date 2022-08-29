from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["office@stoicshirts22.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        return render(redirect, "success.html")


def successView(request):
    messages.success(request, 'Thank you for your message. We will contact you soon')
    return HttpResponseRedirect("contact/success.hmtl")
