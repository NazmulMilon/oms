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
    category = SerializerMethodField()
    assigned_by = SerializerMethodField()
    assigned_to = SerializerMethodField()

    def get_category(self, instance):
        return instance.category.category_name if instance.category else ""

    def get_assigned_by(self, instance):
        return instance.assigned_by.username if instance.assigned_by else ""

    def get_assigned_to(self, instance):
        return instance.assigned_to.username if instance.assigned_to else ""

    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']


class TaskRetrieveSerializer(ModelSerializer):
    category = SerializerMethodField()
    assigned_by = SerializerMethodField()
    assigned_to = SerializerMethodField()

    def get_category(self, instance):
        return instance.category.category_name if instance.category else ""

    def get_assigned_by(self, instance):
        return instance.assigned_by.username if instance.assigned_by else ""

    def get_assigned_to(self, instance):
        return instance.assigned_to.username if instance.assigned_to else ""

    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']
