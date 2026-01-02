
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyUserViewSet, TaskViewSet, StudySessionViewSet, HydrationLogViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'users', StudyUserViewSet, basename='studyuser')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'sessions', StudySessionViewSet, basename='session')
router.register(r'hydration', HydrationLogViewSet, basename='hydration')
router.register(r'reminders', ReminderViewSet, basename='reminder')

urlpatterns = [
    path('api/', include(router.urls)),
]
