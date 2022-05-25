from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.list_all_tasks, name='list-all-tasks'),
    path('create/', views.create_task, name='create-task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete-task'),
    path('<int:task_id>/update/', views.update_task, name='update-task'),
]

