from django.urls import path
from preferences import views


app_name = 'preferences'


urlpatterns = [
    path('add/', views.MyPreferenceFormView.as_view(), name='my-preference-add-view'),
]