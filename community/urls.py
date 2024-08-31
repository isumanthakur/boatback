from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.list_posts, name='list_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<uuid:post_id>/', views.modify_post, name='modify_post'),
    path('posts/<uuid:post_id>/like/', views.like_post, name='like_post'),
    path('posts/<uuid:post_id>/unlike/', views.unlike_post, name='unlike_post'),
    path('posts/<uuid:post_id>/comment/', views.comment_post, name='comment_post'),
]
