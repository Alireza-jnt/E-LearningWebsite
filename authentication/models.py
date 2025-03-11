from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinValueValidator, MaxValueValidator
# from course.models import CourseCategory


class Role(models.Model):
    # role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table = 'roles_name_list'


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    permission_path = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    class Meta:
        db_table = 'permissions'


class PermissionInRole(models.Model):
    permission_in_role_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'permission_in_role'


class NotificationTypes(models.Model):
    NOTIFICATION_TYPE_CATEGORIES = (
        ('course', 'Course'),
        ('account', 'Account'),
        ('marketing', 'Marketing'),
        ('interaction', 'Interaction'),
        ('system', 'System'),
    )
    notification_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=False, null=False)
    description = models.TextField(max_length=255)
    notification_type_category = models.CharField(
        max_length=15,
        choices=NOTIFICATION_TYPE_CATEGORIES,
        default='system'
    )
    default_enabled = models.BooleanField(default=True)

#ToDo
# def get_default_role():
#     return Role.objects.get_or_create(id=3, defaults={'name': 'Default Role'})[0]
get_default_role = 3

class User(AbstractUser):
    GENDER_CHOICES = [
        (True, 'Male'),
        (False, 'Female')
    ]
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    email = models.EmailField(unique=True, null=False, blank=False)
    # role = models.ForeignKey(Role, on_delete=models.PROTECT)
    role = models.ForeignKey(
        'Role',
        on_delete=models.PROTECT,
        default= get_default_role  # Use the callable here
    )
    mobile = models.CharField(max_length=255, unique=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'



class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street_number = models.TextField(null=True, blank=True)
    street_name = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True)
    last_login = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, default='en')
    dark_mode = models.BooleanField(default=False)
    class Meta:
        db_table = 'information'


class UserCategoryPreferences(models.Model):
    user_preferred_categories_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # ToDo
    #  category_id = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    category_type = models.IntegerField()
    is_premium_selection = models.BooleanField(default=False)


class UserNotificationPreferences(models.Model):
    FREQUENCY = (
        ('immediate', 'Immediate'),
        ('never', 'Never'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    )
    user_notification_preference_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type_id = models.ForeignKey(NotificationTypes, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY)





# class UserPreference(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     language = models.CharField(max_length=50, default='en')
#     dark_mode = models.BooleanField(default=False)
#     class Meta:
#         db_table = 'user_preferences'




# class TutorProfile(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     approval_status = models.CharField(
#         max_length=20,
#         choices=[
#             ('pending', 'Pending'),
#             ('approved', 'Approved'),
#             ('rejected', 'Rejected')
#         ],
#         default='pending'
#     )
#     rejection_reason = models.TextField(null=True, blank=True)

