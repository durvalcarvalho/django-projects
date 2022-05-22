from django.urls import path

from images import views

app_name = 'images'


urlpatterns = [
    path('', views.main_view, name='main-view'),
]
