from django.contrib import admin
from src.base.models import User, Task, TaskAttempt, Level, Test, TestAttempt

admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskAttempt)
admin.site.register(Level)
admin.site.register(Test)
admin.site.register(TestAttempt)
