from API.serializers.equipment_serializer import (
    BIGSerializer,
    CannulaSerializer,
    NeedleSerializer,
    SyringeSerializer,
    LtTubeSerializer,
    GauzeSerializer,
    SterileGlovesSerializer,
    GlovesSerializer,
    NasopharyngealTubeSerializer,
    OropharyngealTubeSerializer,
    EndotrachealTubeSerializer,
    LaryngoscopeBladeSerializer,
    OxygenMaskSerializer,
    VentilationMaskSerializer,
    DrugSerializer,
    FluidSerializer,
)

from containers.constants import DRUGS, FLUIDS


API_NAME_CHOICES = [
    "Trauma Wall - ALS",
    "Trauma Wall - hospital",
    "Backpack - ALS",
    "Backpack - ALS Ampoule",
    "Backpack - R1",
    "Bag - R1",
    "Trunk - ALS",
    "Trunk - ALS Ampoule",
    "Storage Drawer - hospital",
    "Special / Other",
]


SERIALIZER_DICT = {
    "BIG": BIGSerializer,
    "Cannula": CannulaSerializer,
    "Needle": NeedleSerializer,
    "Syringe": SyringeSerializer,
    "LT tube": LtTubeSerializer,
    "Gauze": GauzeSerializer,
    "Sterile gloves": SterileGlovesSerializer,
    "Gloves": GlovesSerializer,
    "NPA tube": NasopharyngealTubeSerializer,
    "OPA tube": OropharyngealTubeSerializer,
    "ET tube": EndotrachealTubeSerializer,
    "Laryngoscope blade": LaryngoscopeBladeSerializer,
    "Oxygen mask": OxygenMaskSerializer,
    "Ventilation mask": VentilationMaskSerializer,
}


def serializer_drugs_and_fluids() -> dict:
    for drug, _ in DRUGS:
        SERIALIZER_DICT.update({drug: DrugSerializer})

    for fluid, _ in FLUIDS:
        SERIALIZER_DICT.update({fluid: FluidSerializer})
    print("serializer_dict", SERIALIZER_DICT)
    return SERIALIZER_DICT
