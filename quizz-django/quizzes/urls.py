from django.urls import path
from quizzes import views


app_name = 'quizzes'


urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),

    path('quizzes/<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),
]
