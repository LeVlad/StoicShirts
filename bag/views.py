from django.shortcuts import render


""" A view that returns the shopping bag contents page """


def view_bag(request):
    return render(request, 'bag/bag.html')
