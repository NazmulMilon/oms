from .models import TaskCategory, Task
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField


class TaskCategoryListSerializer(ModelSerializer):
    class Meta:
        model = TaskCategory
        exclude = ['created_at', 'updated_at']


class TaskCategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = TaskCategory
        exclude = ['created_at', 'updated_at']


class TaskCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = TaskCategory
        exclude = ['created_at', 'updated_at']


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']


class TaskRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']
