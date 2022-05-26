from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
]
