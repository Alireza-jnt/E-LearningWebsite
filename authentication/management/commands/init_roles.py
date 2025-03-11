from django.core.management.base import BaseCommand
from authentication.models import Role
from django.db import transaction

class Command(BaseCommand):
    help = 'Initialize default roles for the e-learning platform'

    DEFAULT_ROLES = [
        {
            'id': 1,
            'role_name': 'Root',
            'description': 'Highest level of access with complete system control'
        },
        {
            'id': 2,
            'role_name': 'superuser',
            'description': 'Administrative access with system management capabilities'
        },
        {
            'id': 3,
            'role_name': 'User',
            'description': 'Standard user with basic access to courses and features'
        },
        {
            'id': 4,
            'role_name': 'Instructor',
            'description': 'Course creator with ability to create and manage courses'
        },
        {
            'id': 5,
            'role_name': 'Student',
            'description': 'Learner with access to enrolled courses and learning materials'
        },
        {
            'id': 6,
            'role_name': 'Content Moderator',
            'description': 'User with content moderation and review capabilities'
        }
    ]

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                for role_data in self.DEFAULT_ROLES:
                    role, created = Role.objects.get_or_create(
                        id=role_data['id'],
                        defaults={
                            'role_name': role_data['role_name']
                        }
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Created role: {role_data['role_name']}"
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Role already exists: {role_data['role_name']}"
                            )
                        )

                self.stdout.write(
                    self.style.SUCCESS('Successfully initialized all default roles')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error initializing roles: {str(e)}')
            )
            raise 