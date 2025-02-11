from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import transaction
from .models import Role, Permission, PermissionInRole

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    """
    Creates initial roles and permissions after database migrations.
    This ensures that necessary roles exist before any superuser creation attempts.
    """
    if sender.name == 'authentication':
        with transaction.atomic():
            # Create both Root and Superuser roles
            root_role, created = Role.objects.get_or_create(
                role_name='Root'
            )
            if created:
                print("Created Root role")

            # Create the superuser role that your command expects
            superuser_role, created = Role.objects.get_or_create(
                role_name='superuser'
            )
            if created:
                print("Created Superuser role")

            # Create permissions for both roles
            admin_permission, created = Permission.objects.get_or_create(
                name='Administrator Access',
                defaults={
                    'permission_path': '/*',
                    'is_superuser': True,
                    'is_staff': True
                }
            )
            if created:
                print("Created Administrator permission")

            # Link permissions to roles
            # For Root role
            PermissionInRole.objects.get_or_create(
                role_id=root_role,
                permission_id=admin_permission
            )

            # For Superuser role
            PermissionInRole.objects.get_or_create(
                role_id=superuser_role,
                permission_id=admin_permission
            )
            print("Linked permissions to roles")