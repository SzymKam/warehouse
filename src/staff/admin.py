from django.contrib import admin

from .models import StaffModel


@admin.register(StaffModel)
class StaffAdmin(admin.ModelAdmin):
    pass
    # list_display = (
    #     "position",
    #     "medical_qualifications",
    #     "qualifications_expiration_date",
    # )
    # list_filter = ("position",)
    # search_fields = ("position", "medical_qualifications")
