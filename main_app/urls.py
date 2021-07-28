from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('testing/', views.testing, name='testing'),
    path('vaccines/', views.vaccines, name='vaccines'),
]
