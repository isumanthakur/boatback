from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:property_id>/reviews/add/', views.create_review, name='create_review'),
    path('<uuid:property_id>/reviews/', views.property_reviews, name='property_reviews'),
]
