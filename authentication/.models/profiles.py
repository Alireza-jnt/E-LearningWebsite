from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = (
        (True, _('Male')),
        (False, _('Female'))
    )

    # Override AbstractUser fields for better control
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True)
    email = models.EmailField(_("Email Address"), unique=True)
    username = models.CharField(
        _("Username"),
        max_length=255,
        unique=True,
        help_text=_("Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only.")
    )

    # Custom fields
    role = models.ForeignKey(
        'Role',
        on_delete=models.PROTECT,
        related_name='users',
        verbose_name=_("User Role")
    )
    gender = models.BooleanField(_("Gender"), choices=GENDER_CHOICES)
    mobile = models.CharField(_("Mobile Number"), max_length=20, blank=True, null=True)
    is_deleted = models.BooleanField(_("Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        db_table = 'users'
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['-date_joined']

    def __str__(self):
        return self.get_full_name() or self.username


class AuthorProfile(models.Model):
    APPROVAL_STATUS = (
        ('pending', _('Pending')),
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='author_profile'
    )
    bio = models.TextField(_("Biography"), blank=True)
    score = models.FloatField(_("Author Score"), default=0.0)
    approval_status = models.CharField(
        _("Approval Status"),
        max_length=20,
        choices=APPROVAL_STATUS,
        default='pending'
    )
    rejection_reason = models.TextField(_("Rejection Reason"), blank=True)

    class Meta:
        db_table = 'authors'
        verbose_name = _("Author Profile")
        verbose_name_plural = _("Author Profiles")

    def __str__(self):
        return f"{self.user} - {self.approval_status}"


class UserInformation(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='information'
    )
    profile_picture = models.ImageField(
        _("Profile Picture"),
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    last_login = models.DateTimeField(_("Last Login"), auto_now=True)

    # Address information
    street_number = models.CharField(_("Street Number"), max_length=50, blank=True)
    street_name = models.CharField(_("Street Name"), max_length=255, blank=True)
    state = models.CharField(_("State/Province"), max_length=255, blank=True)

    class Meta:
        db_table = 'information'
        verbose_name = _("User Information")
        verbose_name_plural = _("Users Information")

    def __str__(self):
        return f"{self.user}'s Information"