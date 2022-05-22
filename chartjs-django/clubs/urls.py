from django.urls import path

from clubs import views


urlpatterns = [
    path('', views.ClubChartView.as_view(), name='club-chart'),
]
