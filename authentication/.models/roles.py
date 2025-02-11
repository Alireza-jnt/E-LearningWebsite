from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(_("Role Name"), max_length=255, unique=True)

    class Meta:
        db_table = 'roles'
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(_("Permission Name"), max_length=255)
    codename = models.CharField(_("Code Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        db_table = 'permissions'
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='roles')

    class Meta:
        db_table = 'permission_in_role'
        unique_together = ('role', 'permission')
        verbose_name = _("Role Permission")
        verbose_name_plural = _("Role Permissions")

    def __str__(self):
        return f"{self.role} | {self.permission}"