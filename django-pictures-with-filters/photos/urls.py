from django.urls import path, include

from photos import views

app_name = 'photos'

urlpatterns = [
    path('', views.UploadCreateView.as_view(), name='upload-create'),
]
