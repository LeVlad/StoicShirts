from django.shortcuts import render


""" A view that returns the index """


def index(request):
    return render(request, 'home/index.html')
