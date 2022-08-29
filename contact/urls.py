from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactView, name='contact'),
    path('', views.successView, name='success'),
]
