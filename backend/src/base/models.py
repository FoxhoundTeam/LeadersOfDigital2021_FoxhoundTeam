import json
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)

class Level(models.Model):
    name = models.CharField(max_length=256)

class Task(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    task = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.PROTECT)
    max_attempts = models.PositiveIntegerField(default=1)

    @property
    def task_value(self):
        if isinstance(self.task, list):
            return self.task
        try:
            return json.loads(self.task)
        except:
            return []

    def save(self, *args, **kwargs):
        self.task = json.dumps(self.task_value)
        super().save(*args, **kwargs)

class TeoryInfo(models.Model):
    name = models.CharField(max_length=512)
    info = models.TextField()

class Test(models.Model):
    name = models.CharField(max_length=1024)
    max_attempts = models.PositiveIntegerField(default=1)

class TestTask(models.Model):
    question = models.TextField()
    answers = models.TextField()
    correct_answer = models.CharField(max_length=512)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)

class TaskAttempt(models.Model):
    TYPE_EXAM = 'E'
    TYPE_PRE = 'P'

    TYPES = (
        (TYPE_EXAM, 'Экзамен'),
        (TYPE_PRE, 'Пробная попытка')
    )

    type = models.CharField(max_length=1, choices=TYPES, default=TYPE_PRE)
    dttm_added = models.DateTimeField(auto_now_add=True)
    dttm_start = models.DateTimeField()
    dttm_end = models.DateTimeField(null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    track = models.TextField(default='[]')
    score = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class TestAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    dttm_start = models.DateTimeField(auto_now_add=True)
    dttm_end = models.DateTimeField(null=True, blank=True)

class UserAnswer(models.Model):
    test_attempt = models.ForeignKey(TestAttempt, on_delete=models.PROTECT)
    question = models.ForeignKey(TestTask, on_delete=models.PROTECT)
    answer = models.CharField(max_length=512)
    is_correct = models.BooleanField()
