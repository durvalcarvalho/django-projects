from django.urls import include, path
from repository import views


urlpatterns = [
    path('commits/', views.commits, name='commits'),
]
