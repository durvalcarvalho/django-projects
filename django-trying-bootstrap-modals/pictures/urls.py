from django.urls import path

from pictures.views import PicturesListView, PictureView


urlpatterns = [
    path('', PicturesListView.as_view(), name='pictures_list'),
    path('data-json/', PictureView.as_view(), name='data_json'),
]

