from django.urls import path
from . import views

urlpatterns = [
    path('create/<uuid:property_id>/', views.create_payment, name='create_payment'),
    path('success/', views.payment_success, name='payment_success'),
]
