from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),

    path(
        'posts/',
        views.PostsListView.as_view(),
        name='posts-list-view',
    ),

    path(
        'api/v1/posts/',
        views.JsonPostListView.as_view(),
        name='json-posts-list-view',
    ),
]
