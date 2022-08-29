
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes, name='quotes'),
    path('', views.get_all_quotes, name='quotes'),
]
