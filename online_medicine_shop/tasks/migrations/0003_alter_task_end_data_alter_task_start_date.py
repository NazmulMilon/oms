# Generated by Django 4.1.5 on 2023-01-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_end_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_data',
            field=models.DateTimeField(auto_created=True, help_text=' task end date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(auto_created=True, help_text='task started date'),
        ),
    ]
