from django.conf.urls import url, include
from rest_auth.views import LoginView, LogoutView
from rest_framework import routers
from src.base.views import (
    UserView,
    TaskViewSet,
    TaskAttemptViewSet,
    LevelViewSet,
    TeoryInfoViewSet,
)

rest_auth_urls = [
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserView.as_view(), name='user'),
]

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='Task')
router.register(r'task_attempt', TaskAttemptViewSet, basename='TaskAttempt')
router.register(r'level', LevelViewSet, basename='Level')
router.register(r'teory_info', TeoryInfoViewSet, basename='TeoryInfo')


urlpatterns = [
    url(r'^auth/', include((rest_auth_urls, 'auth'), namespace='auth')),
    url(r'^', include(router.urls)),
]