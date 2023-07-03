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
    MedicalEquipmentSerializer,
)

from containers.constants import DRUGS, FLUIDS, CONTAINER_NAME_CHOICES


def allowed_containers_name():
    api_name_choices = []
    for name, _ in CONTAINER_NAME_CHOICES:
        api_name_choices.append(name)
    api_name_choices.remove("Main warehouse")
    return api_name_choices


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

OTHER_ALLOWED_NAMES = [
    ("Quicktrach", "Quicktrach"),
    ("Spatula", "Spatula"),
    ("LT syringe", "LT syringe"),
    ("LT stabilizer", "LT stabilizer"),
    ("Intubation stylet", "Intubation stylet"),
    ("ET stabilizer", "ET stabilizer"),
    ("Suction catheters", "Suction catheters"),
    ("Magill forceps", "Magill forceps"),
    ("Electric suction", "Electric suction"),
    ("Manual suction", "Manual suction"),
    ("Laryngoscope", "Laryngoscope"),
    ("Decompression Needle", "Decompression Needle"),
    ("Oxygen drain", "Oxygen drain"),
    ("Filter", "Filter"),
    ("Dead space", "Dead space"),
    ("Tracheolife", "Tracheolife"),
    ("Oxygen tank", "Oxygen tank"),
    ("Oxygen reducer", "Oxygen reducer"),
    ("PEEP valve", "PEEP valve"),
    ("Resuscitator", "Resuscitator"),
    ("Respirator", "Respirator"),
    ("Non-sterile swabs", "Non-sterile swabs"),
    ("Surgical suture", "Surgical suture"),
    ("Alcohol swabs", "Alcohol swabs"),
    ("Tactical tourniquet", "Tactical tourniquet"),
    ("Emergency Blanket NRC", "Emergency Blanket NRC"),
    ("Gauze - single", "Gauze - single"),
    ("Chest seal", "Chest seal"),
    ("Hydrogel", "Hydrogel"),
    ("Elastic bandage", "Elastic bandage"),
    ("Knitted bandage", "Knitted bandage"),
    ("Plaster for wound", "Plaster for wound"),
    ("Adhesive tape", "Adhesive tape"),
    ("Triangular bandage", "Triangular bandage"),
    ("Codofix", "Codofix"),
    ("Forceps", "Forceps"),
    ("Scissors", "Scissors"),
    ("Hemostatic dressing", "Hemostatic dressing"),
    ("3-way stopcock", "3-way stopcock"),
    ("Cannula fixation tape", "Cannula fixation tape"),
    ("Skin disinfectant", "Skin disinfectant"),
    ("Sharps disposal containers", "Sharps disposal containers"),
    ("Octenisept", "Octenisept"),
    ("Infusion set", "Infusion set"),
    ("Spike", "Spike"),
    ("Medical tourniquet", "Medical tourniquet"),
    ("Fenistil", "Fenistil"),
    ("Altacet", "Altacet"),
    ("Icemix", "Icemix"),
    ("Pantenol", "Pantenol"),
    ("Glucometer strips", "Glucometer strips"),
    ("Stethoscope", "Stethoscope"),
    ("Pressure gauge", "Pressure gauge"),
    ("Pulse oximeter", "Pulse oximeter"),
    ("Thermometer", "Thermometer"),
    ("Diagnostic flashlight", "Diagnostic flashlight"),
    ("Glucometer", "Glucometer"),
    ("Heart monitor", "Heart monitor"),
    ("Defibrillator", "Defibrillator"),
    ("AED", "AED"),
    ("Capnometer", "Capnometer"),
    ("CPR Meter", "CPR Meter"),
    ("Reflex hammer", "Reflex hammer"),
    ("Triage set", "Triage set"),
    ("USG", "USG"),
    ("Face mask", "Face mask"),
    ("FFP2/3 face mask", "FFP2/3 face mask"),
    ("Waste bags", "Waste bags"),
    ("Protection glasses", "Protection glasses"),
    ("Newborn set", "Newborn set"),
    ("Bladder catheterization set", "Bladder catheterization set"),
    ("Gastric lavage set", "Gastric lavage set"),
    ("Cervical collar", "Cervical collar"),
    ("SAM Splint", "SAM Splint"),
    ("Spine board", "Spine board"),
    ("KED", "KED"),
    ("Pediatric spine board", "Pediatric spine board"),
    ("Scoop stretcher", "Scoop stretcher"),
    ("Vacuum mattress", "Vacuum mattress"),
    ("Kramer splint set", "Kramer splint set"),
    ("Pelvic stabilization belt", "Pelvic stabilization belt"),
    ("Document pad", "Document pad"),
    ("MCR card", "MCR card"),
    ("Paramedic card", "Paramedic card"),
    ("KPP card", "KPP card"),
]


def name_to_serializer() -> dict:
    for drug, _ in DRUGS:
        SERIALIZER_DICT.update({drug: DrugSerializer})
    for fluid, _ in FLUIDS:
        SERIALIZER_DICT.update({fluid: FluidSerializer})
    for element, _ in OTHER_ALLOWED_NAMES:
        SERIALIZER_DICT.update({element: MedicalEquipmentSerializer})
    return SERIALIZER_DICT
