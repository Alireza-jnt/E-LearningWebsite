from django.db import models
# from django.contrib.auth.models import User
from authentication.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    APPROVAL_STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]
    approval_status = models.CharField(max_length=10, choices=APPROVAL_STATUS_CHOICES, default='pending')
    rejection_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Author {self.user.username} - {self.approval_status}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    CATEGORY_TYPES = [
        ('0', 'Category'),
        ('1', 'SubCategory'),
        ('2', 'Sub-Subcategory'),
        ('3', 'Standalone'),
    ]
    type = models.IntegerField(choices=CATEGORY_TYPES,default='3')
    score = models.FloatField(null=True, blank=True,default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Category {self.name}"

class Course(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    price = models.IntegerField()   #models.DecimalField(max_digits=10, decimal_places=3)
    total_lectures = models.IntegerField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')
    language = models.CharField(max_length=50, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    verification_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    rejection_message = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class UserProductReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    approval_status = models.CharField(
        max_length=10,
        choices=Author.APPROVAL_STATUS_CHOICES,
        default='pending',
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.course.title} by {self.user.username}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.course.title}"


class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_name = models.TextField()
    description = models.TextField(null=True, blank=True)
    duration_minutes = models.IntegerField()
    title = models.CharField(max_length=255)

    #Specifies the order in which the sections appear within the course, ensuring they are presented logically
    section_order = models.IntegerField()

    def __str__(self):
        return f"Section {self.title} in {self.course.title}"


class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_address = models.URLField() #ToDo models.FileField(upload_to='files')
    thumbnail = models.URLField(null=True, blank=True) #ToDo models.FileField(upload_to='files')
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    video_order = models.IntegerField() #Must be Per Video section

    def __str__(self):
        return f"Video for {self.course.title} - Section {self.section.title}"

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_term = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched {self.search_term}"
