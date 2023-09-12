from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Container


@receiver(post_migrate)
def create_initial_container(sender, **kwargs):
    if sender.name == "containers":
        Container.objects.get_or_create(
            name="Main warehouse", description="Main warehouse of GRM emergency unit"
        )
