from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission, Group


class StaffConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "staff"

    def ready(self):
        post_migrate.connect(self._create_initial_staff_admin_group, sender=self)
        post_migrate.connect(self._create_initial_container_admin_group, sender=self)

    def _create_initial_staff_admin_group(self, sender, **kwargs):
        from django.contrib.auth.models import Permission, Group

        permission_add_staff = Permission.objects.get(codename="add_staffmodel")
        permission_change_staff = Permission.objects.get(codename="change_staffmodel")
        permission_delete_staff = Permission.objects.get(codename="delete_staffmodel")

        staff_group, created = Group.objects.get_or_create(name="Staff admin group")
        if created:
            staff_group.permissions.add(
                permission_add_staff, permission_change_staff, permission_delete_staff
            )
            staff_group.save()

    def _create_initial_container_admin_group(self, sender, **kwargs):
        from django.contrib.auth.models import Permission, Group

        permission_add_container = Permission.objects.get(codename="add_container")
        permission_change_container = Permission.objects.get(
            codename="change_container"
        )
        permission_delete_container = Permission.objects.get(
            codename="delete_container"
        )
        permission_add_drug = Permission.objects.get(codename="add_drug")
        permission_change_drug = Permission.objects.get(codename="change_drug")
        permission_delete_drug = Permission.objects.get(codename="delete_drug")

        container_group, created = Group.objects.get_or_create(
            name="Container admin group"
        )
        if created:
            container_group.permissions.add(
                permission_add_container,
                permission_change_container,
                permission_delete_container,
                permission_add_drug,
                permission_change_drug,
                permission_delete_drug,
            )
            container_group.save()
