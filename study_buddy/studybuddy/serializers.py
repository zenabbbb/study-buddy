
from rest_framework import serializers
from .models import StudyUser, Task, StudySession, HydrationLog, Reminder

class StudyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyUser
        fields = "__all__"
        read_only_fields = ("tasks_done_total", "created_at", "updated_at")

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "completed_at")

class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = "__all__"
        read_only_fields = ("created_at",)

class HydrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydrationLog
        fields = "__all__"
        read_only_fields = ("timestamp",)

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
        read_only_fields = ("created_at",)
