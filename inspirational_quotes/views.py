from django.shortcuts import render, get_list_or_404
from .models import InspirationalQuote


def get_all_quotes(request):
    """ A view to get all the stoic quotes """
    name = get_list_or_404(InspirationalQuote)
    quote = InspirationalQuote.objects.all()
    custom_name = get_list_or_404(InspirationalQuote)
    stoic_idea = get_list_or_404(InspirationalQuote)
    context = {
        'name': name,
        'custom_name': custom_name,
        'quote': quote,
        'stoic_idea': stoic_idea
    }
    return render(request, 'quotes/quotes.html', context)
