from django.db import models
from django.contrib.auth.models import User


# Создаем базовый класс для моделей с одинаковыми полями
class BaseAdaptModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # указываем true, чтобы не создавалась данныя таблица


# class User(models.Model):
#     first_name = models.CharField(max_length=64, null=False)
#     last_name = models.CharField(max_length=64, null=False)
#     login = models.CharField(max_length=64, unique=True, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     position_in_comp = models.ForeignKey('PositionInComp', on_delete=models.SET_NULL)


class PositionInComp(BaseAdaptModel):
    pass


class Category(BaseAdaptModel):
    pass


class Priority(BaseAdaptModel):
    pass


class TaskType(BaseAdaptModel):
    pass


class Plan(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='plans')
    position_id = models.ForeignKey('PositionInComp', on_delete=models.CASCADE, related_name='plans')
    priority_id = models.ForeignKey('Priority', on_delete=models.CASCADE, related_name='plans')
    description = models.CharField(max_length=500, default='План адаптации')
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    sequence = models.IntegerField()
    plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE, related_name='tasks')
    task_type_id = models.ForeignKey('TaskType', on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserPlan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plans')
    plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE, related_name='users')
    deadline = models.DateField(null=True)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserTaskStatus(models.Model):
    user_plan_id = models.ForeignKey('UserPlan', on_delete=models.CASCADE, related_name='tasks_status')
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='tasks_status')
    end_date = models.DateField(null=True)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
