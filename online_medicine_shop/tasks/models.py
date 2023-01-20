from django.db import models
from systems.models import BaseModel
from django.contrib.auth.models import User
from systems.enums import TaskStatusType


class TaskCategory(BaseModel):
    category_name = models.CharField(max_length=100, help_text='task category name')

    class Meta:
        db_table = 'task_categories'


class Task(BaseModel):
    title = models.CharField(max_length=200, help_text=' title of the task')
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, help_text='task category name')
    start_date = models.DateTimeField(auto_created=True, help_text='task started date')
    end_date = models.DateTimeField(auto_created=True, help_text=' task end date')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks',
                                    help_text='person who assigned the task')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',
                                    help_text='person who will do the task')
    details = models.TextField(help_text='task details')
    task_status = models.CharField(max_length=100, choices=TaskStatusType.choices(), default=TaskStatusType.ASSIGNED.value,
                                   help_text='current status of the task')

    class Meta:
        db_table = 'tasks'
