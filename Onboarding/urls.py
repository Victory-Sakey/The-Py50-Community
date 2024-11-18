from django.urls import path
from . import views

app_name = 'Onboarding'

urlpatterns = [
    path('pyguide', views.Onboarding, name='Onboarding'),
    path('', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('join', views.join_community, name='join'),
    path('tutor', views.tutor, name='tutor'),
    path('mentor', views.mentor, name='mentor'),
    path('scholar', views.scholar, name='scholar'),
    path('scholar/registration', views.scholar_registration, name='scholar_registration'),
    path('scholar/registration/payment/', views.payment, name='payment'),
]