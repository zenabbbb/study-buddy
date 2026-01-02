
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class StudyUser(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('nonbinary', 'Non-binary'),
        ('other', 'Other'),
        ('prefer_not', 'Prefer not to say'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    streak = models.IntegerField(default=0)
    tasks_done_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Task(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_INPROG = 'in-progress'
    STATUS_DONE = 'done'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_INPROG, 'In Progress'),
        (STATUS_DONE, 'Done'),
    ]

    user = models.ForeignKey(StudyUser, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_done(self):
        if self.status != self.STATUS_DONE:
            self.status = self.STATUS_DONE
            self.completed_at = timezone.now()
            self.save(update_fields=['status', 'completed_at', 'updated_at'])

    def __str__(self):
        return f"{self.title} ({self.user.name})"


class StudySession(models.Model):
    user = models.ForeignKey(StudyUser, on_delete=models.CASCADE, related_name="sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    breaks_taken = models.IntegerField(default=0)
    blinks = models.IntegerField(default=0)
    liters_drank = models.FloatField(default=0.0)
    emotions = models.JSONField(default=list, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def end(self, end_time=None):
        self.end_time = end_time or timezone.now()
        self.save(update_fields=['end_time'])

    def __str__(self):
        return f"Session {self.id} - {self.user.name} - {self.start_time.isoformat()}"


class HydrationLog(models.Model):
    user = models.ForeignKey(StudyUser, on_delete=models.CASCADE, related_name="hydration_logs")
    timestamp = models.DateTimeField(auto_now_add=True)
    amount_ml = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.amount_ml} ml @ {self.timestamp}"


class Reminder(models.Model):
    TYPE_CHOICES = [
        ('hydration', 'Hydration'),
        ('stretch', 'Stretch'),
        ('eye_break', 'Eye Break'),
        ('nap', 'Nap'),
        ('task', 'Task'),
        ('custom', 'Custom'),
    ]
    STATUS_SENT = 'sent'
    STATUS_SNOOZED = 'snoozed'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = [
        (STATUS_SENT, 'Sent'),
        (STATUS_SNOOZED, 'Snoozed'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    user = models.ForeignKey(StudyUser, on_delete=models.CASCADE, related_name="reminders")
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SENT)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    recurrence = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def mark_completed(self):
        self.status = self.STATUS_COMPLETED
        self.save(update_fields=['status'])

    def __str__(self):
        return f"{self.user.name} - {self.type} @ {self.scheduled_for or self.timestamp}"
