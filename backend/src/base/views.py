from rest_framework import viewsets
from src.base.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import UserDetailsView
from src.base.models import (
    Level, 
    Task,
    TaskAttempt,
    Test,
    TeoryInfo,
    TestAttempt,
)
from src.base.serializers import (
    LevelSerializer, 
    TaskSeializer, 
    TaskAttemptSerializer,
    TestSerializer,
    UserSerializer,
    TeoryInfoSerializer,
    TestAttemptSerializer,
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

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdminOrReadOnly,]

class TestAttemptViewSet(viewsets.ModelViewSet):
    queryset = TestAttempt.objects.all()
    serializer_class = TestAttemptSerializer
    permission_classes = [IsAuthenticated,]
