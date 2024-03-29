from django.urls import path
from . import views
app_name='posts'

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<str:username>/', views.UserPost.as_view(), name='for_user'),
    path('by<slug:username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]
