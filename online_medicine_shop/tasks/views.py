from django.shortcuts import render
from .models import Task, TaskCategory
from .serilizers import TaskCategoryCreateSerializer, TaskCategoryListSerializer, TaskCategoryRetrieveSerializer, \
    TaskListSerializer, TaskCreateSerializer, TaskRetrieveSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema


class TaskCategoryListAPIView(ListAPIView):
    serializer_class = TaskCategoryListSerializer
    queryset = TaskCategory.objects.all()

    @swagger_auto_schema(tags=['Task Category'])
    def get(self, request, *args, **kwargs):
        queryset = TaskCategory.objects.all()
        serializer = TaskCategoryListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TaskCategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = TaskCategoryRetrieveSerializer
    queryset = TaskCategory.objects.all()

    @swagger_auto_schema(tags=['Task Category'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_obj = TaskCategory.objects.filter(pk=pk).first()
        serializer = TaskCategoryRetrieveSerializer(category_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TaskCategoryCreateAPIView(CreateAPIView):
    serializer_class = TaskCategoryCreateSerializer
    queryset = TaskCategory.objects.all()

    @swagger_auto_schema(tags=['Task Category'])
    def post(self, request, *args, **kwargs):
        data = request.data
        category_name = data.get('category_name', None)
        category_obj = TaskCategory(category_name=category_name)
        category_obj.save()
        return Response(data={'details': 'Task Category Created'}, status=status.HTTP_201_CREATED)


class TaskListAPIView(ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()

    @swagger_auto_schema(tags=['Task'])
    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = TaskListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TaskRetrieveAPIView(RetrieveAPIView):
    serializer_class = TaskRetrieveSerializer
    queryset = Task.objects.all()

    @swagger_auto_schema(tags=['Task'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        task_obj = Task.objects.filter(pk=pk).first()
        serializer = TaskRetrieveSerializer(task_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        title = data.get('title', None)
        category = data.get('category', None)
        assigned_by = data.get('assigned_by', None)
        assigned_to = data.get('assigned_to', None)
        details = data.get('details', None)
        task_status = data.get('task_status', None)
        start_date = data.get('start_date', None)
        end_date = data.get('start_date', None)

        task_obj = Task(title=title, category_id=category, assigned_by_id=assigned_by, assigned_to_id=assigned_to,
                        details=details, task_status=task_status, start_date=start_date, end_date=end_date)
        task_obj.save()
        serializer = TaskRetrieveSerializer(task_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
