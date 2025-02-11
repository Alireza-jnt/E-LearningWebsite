from django.db import models
from django.contrib.auth.models import User
from .course_models import Course, CourseSection

class Enrollment(models.Model):
    order_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    last_accessed = models.DateTimeField(auto_now=True)
    total_time_spent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.completion_percentage}%)"


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    duration = models.TimeField()

    def __str__(self):
        return self.name


class SubscriptionPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.title} - {self.subscription_type.name}"


class Question(models.Model):
    IS_APPROVED_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True, blank=True)
    file_upload = models.URLField(null=True, blank=True)
    asked_at = models.DateTimeField(auto_now_add=True)
    response_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="responses")
    response = models.TextField(null=True, blank=True)
    response_at = models.DateTimeField(null=True, blank=True)
    is_approved = models.CharField(max_length=10, choices=IS_APPROVED_CHOICES, default='pending')
    is_deleted = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approvers")
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.asked_by.username}: {self.question_text[:30]}..."
