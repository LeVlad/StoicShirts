from django.shortcuts import render, get_list_or_404
from .models import Quote


def get_all_quotes(request):
    """ A view to get all the stoic quotes """
    name = get_list_or_404(Quote)
    quotes = Quote.objects.all()
    custom_name = get_list_or_404(Quote)
    context = {
        'name': name,
        'custom_name': custom_name,
        'quotes': quotes,
    }
    return render(request, 'quotes/quotes.html', context)
