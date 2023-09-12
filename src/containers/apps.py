from django.apps import AppConfig


class ContainersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "containers"

    def ready(self):
        import containers.signals
