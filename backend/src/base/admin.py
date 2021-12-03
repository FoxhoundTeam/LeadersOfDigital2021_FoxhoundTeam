from django.contrib import admin
from src.base.models import User, Task, TaskAttempt, Level

admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskAttempt)
admin.site.register(Level)
