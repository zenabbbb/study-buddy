
from rest_framework import viewsets, filters
from .models import StudyUser, Task, StudySession, HydrationLog, Reminder
from .serializers import (
    StudyUserSerializer, TaskSerializer, StudySessionSerializer,
    HydrationLogSerializer, ReminderSerializer
)

class StudyUserViewSet(viewsets.ModelViewSet):
    queryset = StudyUser.objects.all().order_by('-created_at')
    serializer_class = StudyUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'user__name']

class StudySessionViewSet(viewsets.ModelViewSet):
    queryset = StudySession.objects.all().order_by('-start_time')
    serializer_class = StudySessionSerializer

class HydrationLogViewSet(viewsets.ModelViewSet):
    queryset = HydrationLog.objects.all().order_by('-timestamp')
    serializer_class = HydrationLogSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all().order_by('-timestamp')
    serializer_class = ReminderSerializer
