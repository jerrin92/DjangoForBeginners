from django.urls import path, include
from .views import BlogListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]