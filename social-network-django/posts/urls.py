from django.urls import path
from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.post_comment_create_and_list_view, name='main-post-view'),
    path('like-or-unlike-post/', views.like_or_unlike_post, name='like-or-unlike-post'),

    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),

]