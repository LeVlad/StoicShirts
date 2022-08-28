from django.shortcuts import render, get_list_or_404



def get_all_quotes(request):
    """ A view to get all the stoic quotes """
    quotes = StoicQuotes.objects.all()
    stoic = get_list_or_404('stoic')
    context = {
        'stoic': stoic,
        'quotes': quotes,
    }
    return render(request, 'quotes/quotes.html', context)
