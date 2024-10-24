from django.apps import AppConfig


class DiytoursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diytours'
    def ready(self):
        from .models import Media
