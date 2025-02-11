from django.db import models
from django.contrib.auth import get_user_model
from .course_models import Course, CourseSection

User = get_user_model()

class Enrollment(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    final_price = models.CharField(max_length=255)

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    completion_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    last_accessed = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.IntegerField(null=True, blank=True)

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    duration = models.DurationField()

class SubscriptionPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    APPROVAL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    asked_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions_asked'
    )
    question_text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(
        CourseSection,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    file_upload = models.CharField(max_length=255, null=True, blank=True)
    asked_at = models.DateTimeField(auto_now_add=True)
    response_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions_answered'
    )
    response = models.TextField()
    response_at = models.DateTimeField()
    is_approved = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS_CHOICES,
        default='pending'
    )
    is_deleted = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions_approved'
    )
    approved_at = models.DateTimeField()