from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

#employee/ admin dashboard views
@login_required
def admin_dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'admin_dashboard.html', {'tasks': tasks})

@login_required
def employee_dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'employee_dashboard.html', {'tasks': tasks})


@login_required
@require_POST
def mark_done(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        assigned_to=request.user
    )
    task.status = 'done'
    task.save()
    return redirect('employee-dashboard')

#admin dashboard views
def is_manager(user):
    return user.is_staff

# ADMIN / MANAGER DASHBOARD in UI
@login_required
@user_passes_test(is_manager)
def admin_dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'admin_dashboard.html', {'tasks': tasks})

# CREATE / ASSIGN TASK options in UI
@login_required
@user_passes_test(is_manager)
def create_task(request):
    employees = User.objects.filter(is_staff=False)

    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            assigned_to_id=request.POST['assigned_to'],
            deadline=request.POST['deadline']
        )
        return redirect('admin-dashboard')

    return render(request, 'create_task.html', {'employees': employees})

#delete task options in Ui
@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('admin-dashboard')

#create employee options in ui
@login_required
@user_passes_test(lambda u: u.is_staff)
def create_employee(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            is_staff=False
        )
        return redirect('admin-dashboard')

    return render(request, 'create_employee.html')
