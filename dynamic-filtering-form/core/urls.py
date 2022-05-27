from django.urls import path

from core import views

urlpatterns = [
    path('', views.boostrap_filter_view, name='boostrap_filter'),
    path('automatic/', views.automatic_filter_view, name='automatic_filter'),
]
