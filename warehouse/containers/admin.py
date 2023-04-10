from django.contrib import admin
from .models import (
    MedicalEquipment,
    Container,
    Drug,
    Cannula,
    EndotrachealTube,
    Fluid,
    Gauze,
    Gloves,
    VentilationMask,
    OxygenMask,
    OropharyngealTube,
    NasopharyngealTube,
    LaryngoscopeBlade,
    BIG,
    LTTube,
    Needle,
    Syringe,
    SterileGloves,
)


@admin.register(
    Drug,
    Cannula,
    EndotrachealTube,
    Fluid,
    Gauze,
    Gloves,
    VentilationMask,
    OxygenMask,
    OropharyngealTube,
    NasopharyngealTube,
    LaryngoscopeBlade,
    BIG,
    LTTube,
    Needle,
    Syringe,
    SterileGloves,
)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass
