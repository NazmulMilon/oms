from django.urls import path
from .views import TaskCategoryListAPIView, TaskCategoryRetrieveAPIView, TaskCategoryCreateAPIView, TaskListAPIView, \
    TaskRetrieveAPIView, TaskCreateAPIView, TaskCategoryUpdateAPIView

urlpatterns = [
    path('task/category/list/all/', TaskCategoryListAPIView.as_view(), name='task_category_list'),
    path('task/category/detail/<int:pk>/', TaskCategoryRetrieveAPIView.as_view(), name='task_category_detail'),
    path('task/category/create/', TaskCategoryCreateAPIView.as_view(), name='task_category_create'),
    path('task/category/update/<int:pk>/', TaskCategoryUpdateAPIView.as_view(), name='task_category_update'),

    path('task/list/all/', TaskListAPIView.as_view(), name='task_list'),
    path('task/detail/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),

]