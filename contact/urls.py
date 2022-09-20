from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactView, name='contact'),
    path('contact/success/', views.successView, name='success'),
    path('contact/subscribe/', views.subscribeView, name='subscribe'),
]
