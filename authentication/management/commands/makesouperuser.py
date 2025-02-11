from authentication.models import Role, User, UserInformation
from django.core.management import BaseCommand
from django.db import transaction

class Command(BaseCommand):
    help = 'Create a superuser with additional fields'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                # Ensure the superuser role exists
                role, created = Role.objects.get_or_create(
                    role_name='superuser'
                )
                if created:
                    self.stdout.write(self.style.SUCCESS("Created superuser role as it didn't exist."))

                username = input("Username: ")
                email = input("Email address: ")
                password = input("Password: ")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                gender_input = input("Gender (M/F): ")
                gender = True if gender_input.lower() == 'm' else False

                # Create the user
                user = User.objects.create(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    is_staff=True,
                    is_superuser=True
                )
                user.set_password(password)
                user.save()

                # Create user information
                UserInformation.objects.create(user=user)

                self.stdout.write(self.style.SUCCESS(f"Superuser {username} created successfully."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating superuser: {str(e)}"))
            return