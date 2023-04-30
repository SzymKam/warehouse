from django.contrib import admin
from .models import StaffModel


@admin.register(StaffModel)
class StaffAdmin(admin.ModelAdmin):
    pass
