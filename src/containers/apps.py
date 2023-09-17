from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ContainersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "containers"

    def ready(self):
        post_migrate.connect(self._create_initial_container, sender=self)

    def _create_initial_container(self, sender, **kwargs):
        from .models import Container

        Container.objects.get_or_create(
            name="Main warehouse", description="Main warehouse of GRM emergency unit"
        )
