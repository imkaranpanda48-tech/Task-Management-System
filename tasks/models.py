from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )
    deadline = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending'
    )

    def __str__(self):
        return self.title
