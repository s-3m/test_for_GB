from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=64, null=False),
    last_name = models.CharField(max_length=64, null=False),
    login = models.CharField(max_length=64, unique=True, null=False),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class PositionInComp(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class PlanType(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class Priority(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class Plan(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE),
    plan_type_id = models.ForeignKey('PlanType', on_delete=models.CASCADE),
    position_id = models.ForeignKey('Position', on_delete=models.CASCADE),
    priority_id = models.ForeignKey('Priority', on_delete=models.CASCADE),
    description = models.CharField(max_length=500, default='План адаптации'),
    is_published = models.BooleanField(default=True),
    is_active = models.BooleanField(default=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class TaskType(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    sequence = models.IntegerField(),
    plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE),
    task_type_id = models.ForeignKey('TaskType', on_delete=models.CASCADE),
    description = models.CharField(max_length=500, null=False),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class UserPlan(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE),
    plan_id = models.ForeignKey('Plan', on_delete=models.CASCADE),
    deadline = models.DateField(),
    is_finished = models.BooleanField(default=False),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)


class UserTaskStatus(models.Model):
    user_plan_id = models.ForeignKey('UserPlan', on_delete=models.CASCADE),
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE),
    end_date = models.DateField(),
    is_finished = models.BooleanField(default=False),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)
