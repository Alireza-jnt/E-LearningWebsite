from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
    def ready(self):
        # Import signals when the app is ready
        # This ensures all models are loaded before signals are connected
        import authentication.signals