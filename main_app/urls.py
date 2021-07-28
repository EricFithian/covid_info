from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('testing/', views.testing, name='testing'),
    path('testing/<int:id>/', views.testing_lookup, name='testing-detail'),
    path('testing/<int:id>/delete/', views.test_delete, name='testing-delete'),
    path('vaccines/', views.vaccines, name='vaccines'),
]
