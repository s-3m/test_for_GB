# Generated by Django 4.1.3 on 2022-11-24 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adaptapp', '0004_alter_userplan_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='adaptapp.category'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='adaptapp.positionincomp'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='priority_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='adaptapp.priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='adaptapp.plan'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='adaptapp.tasktype'),
        ),
        migrations.AlterField(
            model_name='userplan',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='adaptapp.plan'),
        ),
        migrations.AlterField(
            model_name='userplan',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='adaptapp.user'),
        ),
        migrations.AlterField(
            model_name='usertaskstatus',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usertaskstatus',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_status', to='adaptapp.task'),
        ),
        migrations.AlterField(
            model_name='usertaskstatus',
            name='user_plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_status', to='adaptapp.userplan'),
        ),
    ]
