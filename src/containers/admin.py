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
    LtTube,
    Needle,
    Syringe,
    SterileGloves,
)


admin.site.register(SterileGloves)
admin.site.register(Syringe)
admin.site.register(Needle)
admin.site.register(LtTube)
admin.site.register(BIG)
admin.site.register(LaryngoscopeBlade)
admin.site.register(NasopharyngealTube)
admin.site.register(OropharyngealTube)
admin.site.register(OxygenMask)
admin.site.register(VentilationMask)
admin.site.register(Gloves)
admin.site.register(Gauze)
admin.site.register(Fluid)
admin.site.register(Drug)
admin.site.register(Cannula)
admin.site.register(EndotrachealTube)
admin.site.register(MedicalEquipment)
admin.site.register(Container)
