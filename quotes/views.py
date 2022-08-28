from django.shortcuts import render, get_list_or_404
from.models import Philosopher

def quotes(request):
    quotes = None
    philosopher = get_list_or_404(Philosopher)
    context = {
        'philosopher': philosopher,
        'quotes': quotes,
    }
    return render(request, 'quotes/quotes.html', context)
