
from django.contrib import admin
from .models import StudyUser, Task, StudySession, HydrationLog, Reminder

@admin.register(StudyUser)
class StudyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'streak', 'tasks_done_total', 'created_at')
    search_fields = ('name', 'email')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'deadline', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description', 'user__name')

@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_time', 'end_time', 'breaks_taken', 'blinks', 'liters_drank')

@admin.register(HydrationLog)
class HydrationLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount_ml', 'timestamp')
    search_fields = ('user__name',)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'status', 'scheduled_for', 'timestamp')
    list_filter = ('type', 'status')
