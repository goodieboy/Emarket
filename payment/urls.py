from django.urls import path
from . import views

urlpatterns = [
    path('', views.initiate_payment, name='initiate_payment'),
    path('test/', views.test, name='test'),
    path('<str:ref>/', views.verify_payment, name='verify_payment'),
]
