from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import admin_dashboard, employee_dashboard, mark_done, create_task, delete_task, create_employee

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('employee-dashboard/', employee_dashboard, name='employee-dashboard'),
    path('task-done/<int:task_id>/', mark_done, name='task-done'),
    path('create-task/', create_task, name='create-task'),
    path('task-delete/<int:task_id>/', delete_task, name='task-delete'),
    path('employee-create/', create_employee, name='employee-create'),

]
