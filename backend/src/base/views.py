from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from src.base.permissions import IsAdmin, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import UserDetailsView
from src.base.models import (
    Level, 
    Task,
    TaskAttempt,
    Test,
    TeoryInfo,
)
from src.base.serializers import (
    ChartSerializer, 
    LevelSerializer, 
    TaskSeializer, 
    TaskAttemptSerializer,
    TestSerializer,
    UserSerializer,
    TeoryInfoSerializer,
)

class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated,]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSeializer
    permission_classes = [IsAdminOrReadOnly,]

class TaskAttemptViewSet(viewsets.ModelViewSet):
    queryset = TaskAttempt.objects.all()
    serializer_class = TaskAttemptSerializer
    permission_classes = [IsAuthenticated,]

class UserView(UserDetailsView):
    serializer_class = UserSerializer


class TeoryInfoViewSet(viewsets.ModelViewSet):
    queryset = TeoryInfo.objects.all()
    serializer_class = TeoryInfoSerializer
    permission_classes = [IsAdminOrReadOnly,]
