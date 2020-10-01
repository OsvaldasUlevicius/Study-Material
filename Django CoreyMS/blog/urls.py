from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), # just pk is enough
    path('post/new', PostCreateView.as_view(), name='post-create'), # just pk is enough
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # just pk is enough
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # just pk is enough
    path('about/', views.about, name='blog-about'),
]