from django.urls import path

from todos import views


app_name = 'todos'


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('', views.TaskList.as_view(), name='task_list'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),

    path('<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]
