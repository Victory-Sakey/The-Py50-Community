from django.urls import path
from . import views

app_name = 'Onboarding'

urlpatterns = [
    path('pyguide', views.Onboarding, name='Onboarding'),
    path('', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('join', views.join_community, name='join'),
]