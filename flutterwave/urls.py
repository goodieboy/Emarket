from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_payment, name='start_payment'),
    path('<str:id>/', views.payment_verification, name='payment_verification'),
]