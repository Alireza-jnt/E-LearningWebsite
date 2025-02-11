from django.db import models
from django.utils.translation import gettext_lazy as _


class UserPreference(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='preferences'
    )
    language = models.CharField(
        _("Interface Language"),
        max_length=10,
        default='en',
        help_text=_("ISO language code (e.g., en, es, fr)")
    )
    dark_mode = models.BooleanField(
        _("Dark Mode"),
        default=False,
        help_text=_("Enable dark theme for the interface")
    )

    class Meta:
        db_table = 'user_preferences'
        verbose_name = _("User Preference")
        verbose_name_plural = _("User Preferences")

    def __str__(self):
        return f"{self.user}'s Preferences"


class NotificationType(models.Model):
    NOTIFICATION_CATEGORIES = (
        ('course', _('Course')),
        ('account', _('Account')),
        ('marketing', _('Marketing')),
        ('interaction', _('Interaction')),
        ('system', _('System')),
    )

    name = models.CharField(_("Notification Type"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    category = models.CharField(
        _("Category"),
        max_length=20,
        choices=NOTIFICATION_CATEGORIES,
        default='system'
    )
    default_enabled = models.BooleanField(_("Enabled by Default"), default=True)

    class Meta:
        db_table = 'notification_types'
        verbose_name = _("Notification Type")
        verbose_name_plural = _("Notification Types")

    def __str__(self):
        return self.name


class UserNotificationPreference(models.Model):
    FREQUENCY_CHOICES = (
        ('immediate', _('Immediate')),
        ('daily', _('Daily Digest')),
        ('weekly', _('Weekly Digest')),
        ('never', _('Never')),
    )

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='notification_preferences'
    )
    notification_type = models.ForeignKey(
        NotificationType,
        on_delete=models.CASCADE,
        related_name='user_preferences'
    )
    is_enabled = models.BooleanField(_("Enabled"), default=True)
    frequency = models.CharField(
        _("Notification Frequency"),
        max_length=10,
        choices=FREQUENCY_CHOICES,
        default='immediate'
    )

    class Meta:
        db_table = 'user_notification_preferences'
        unique_together = ('user', 'notification_type')
        verbose_name = _("User Notification Preference")
        verbose_name_plural = _("User Notification Preferences")

    def __str__(self):
        return f"{self.user} - {self.notification_type}"


class UserCategoryPreference(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='category_preferences'
    )
    category = models.ForeignKey(
        'courses.Category',
        on_delete=models.CASCADE,
        related_name='user_preferences'
    )
    category_type = models.PositiveSmallIntegerField(_("Category Type"))
    is_premium_selection = models.BooleanField(
        _("Premium Selection"),
        default=False,
        help_text=_("Marked as preferred premium category")
    )

    class Meta:
        db_table = 'user_category_preferences'
        unique_together = ('user', 'category', 'category_type')
        verbose_name = _("User Category Preference")
        verbose_name_plural = _("User Category Preferences")

    def __str__(self):
        return f"{self.user} - {self.category}"