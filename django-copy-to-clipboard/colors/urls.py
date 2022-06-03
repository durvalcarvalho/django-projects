from django.urls import path

from colors.views import ColorListView


urlpatterns = [
    path('', ColorListView.as_view(), name='list_colors'),
]
