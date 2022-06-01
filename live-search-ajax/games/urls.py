from django.urls import path

from games import views

app_name = ' '

urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
    path('<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]

