from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('repair/<int:repair_id>/', views.repair_detail, name='repair_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
