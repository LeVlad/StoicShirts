from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LWUwfA9a2OdEjKGRC4RlJrgEzTqABwX5EdHNr3dLCDJedDtQR0a5NJX0nZPDAxzXaG0Vui743mNN3xQY1wXskcs00ET0ECVvx',
        'client_secret_key': 'client secret key'
    }

    return render(request, template, context)