from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail'),  # Use 'id' as the lookup field

    path('blogposts/list/', views.BlogPostList.as_view(), name='blogpost-list'),  # List all blog posts
    ]