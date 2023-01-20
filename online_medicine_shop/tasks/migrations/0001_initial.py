# Generated by Django 4.1.5 on 2023-01-20 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(help_text='task category name', max_length=100)),
            ],
            options={
                'db_table': 'task_categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_data', models.DateTimeField(auto_created=True, help_text=' task end date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text=' title of the task', max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True, help_text='task started date')),
                ('details', models.TextField(help_text='task details')),
                ('task_status', models.CharField(choices=[('assigned', 'ASSIGNED'), ('not_assigned', 'NOT_ASSIGN'), ('completed', 'COMPLETED'), ('running', 'RUNNING'), ('pause', 'PAUSE')], default='assigned', help_text='current status of the task', max_length=100)),
                ('assigned_by', models.ForeignKey(help_text='person who assigned the task', on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(help_text='person who will do the task', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(help_text='task category name', on_delete=django.db.models.deletion.CASCADE, to='tasks.taskcategory')),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
