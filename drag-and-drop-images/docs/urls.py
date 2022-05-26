from django.urls import path

from docs import views

app_name = 'docs'

urlpatterns = [
    path('', views.MainView.as_view(), name='main-view'),
    path('upload/', views.FileUploadView.as_view(), name='file-upload-view'),
]
