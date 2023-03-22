DRUGS = sorted(
    [
        ("Adrenalin", "Adrenalin"),
        ("ASA", "ASA"),
        ("Ketonal", "Ketonal"),
        ("Ibuprofen", "Ibuprofen"),
        ("Pyralgin", "Pyralgin"),
        ("Paracetamol", "Paracetamol"),
        ("Morphine", "Morphine"),
        ("Fentanyl", "Fentanyl"),
        ("Naloxone", "Naloxone"),
        ("Budesonide", "Budesonide"),
        ("Hydrocortisone", "Hydrocortisone"),
        ("Dexaven", "Dexaven"),
        ("Relanium", "Relanium"),
        ("Relsed", "Relsed"),
        ("Clonazepam", "Clonazepam"),
        ("Midanium", "Midanium"),
        ("Flumazenil", "Flumazenil"),
        ("Atropine", "Atropine"),
        ("Adenosine", "Adenosine"),
        ("Amiodarone", "Amiodarone"),
        ("Lidocaine", "Lidocaine"),
        ("Salbutamol", "Salbutamol"),
        ("Urapidil", "Urapidil"),
        ("Betaloc", "Betaloc"),
        ("No-Spa", "No-Spa"),
        ("Nitromind", "Nitromid"),
        ("Clopidogrel", "Clopidogrel"),
        ("Ticagrelor", "Ticagrelor"),
        ("Heparin", "Heparin"),
        ("Torecan", "Torecan"),
        ("Metoclopramide", "Metoclopramide"),
        ("Furosemide", "Furosemide"),
        ("Mannitol", "Mannitol"),
        ("Hydroxyzine", "Hydroxyzine"),
        ("Magnesium", "Magnesium"),
        ("Clemastine", "Clemastine"),
        ("Bicarbonate", "Bicarbonate"),
        ("Captopril", "Captopril"),
        ("Glucagon", "Glucagon"),
        ("Glucose 20%", "Glucose 20%"),
        ("Glucose 40%", "Glucose 40%"),
        ("Glucose 5%", "Glucose 5%"),
        ("NaCl 0.9%", "NaCl 0.9%"),
        ("Optilyte", "Optilyte"),
        ("Ringer", "Ringer"),
        ("Plasmalyte", "Plasmalyte"),
        ("Exacyl", "Exacyl"),
        ("Ketamine", "Ketamine"),
        ("Polstigmine", "Polstigmine"),
        ("Ondansetron", "Ondansetron"),
        ("Buscolysin", "Buscolysin"),
        ("Suxamethonium", "Suxamethonium"),
        ("Calcium", "Calcium"),
        ("Propofol", "Propofol"),
        ("Pantoprazol", "Pantoprazol"),
        ("Aqua", "Aqua"),
        ("Nitrendipine", "Nitrendipine"),
        ("Rocuronium", "Rocuronium"),
    ]
)

DISPOSABLE_EQUIPMENT = [
    ("Cannula", "Cannula"),
    ("BIG", "BIG"),
    ("3-way stopcock", "3-way stopcock"),
    ("Cannula fixation tape", "Cannula fixation tape"),
    ("Skin disinfectant", "Skin disinfectant"),
    ("Sharps disposal containers", "Sharps disposal containers"),
    ("Needle", "Needle"),
    ("Syringe", "Syringe"),
    ("Glucometer strips", "Glucometer strips"),
    ("Infusion set", "Infusion set"),
    ("Quicktrach", "Quicktrach"),
    ("Decompression Needle", "Decompression Needle"),
    ("NPA tube", "NPA tube"),
    ("Spatula", "Spatula"),
    ("OPA tube", "OPA tube"),
    ("LT syringe", "LT syringe"),
    ("LT stabilizer", "LT stabilizer"),
    ("Tracheolife", "Tracheolife"),
    ("LT tube", "LT tube"),
    ("Intubation stylet", "Intubation stylet"),
    ("ET stabilizer", "ET stabilizer"),
    ("ET tube", "ET tube"),
    ("Oxygen drain", "Oxygen drain"),
    ("Filter", "Filter"),
    ("Ventilation mask", "Ventilation mask"),
    ("Dead space", "Dead space"),
    ("Suction catheters", "Suction catheters"),
    ("Newborn set", "Newborn set"),
    ("Oxygen mask", "Oxygen mask"),
    ("Face mask", "Face mask"),
    ("FFP2/3 face mask", "FFP2/3 face mask"),
    ("Spike", "Spike"),
    ("Sterile gloves", "Sterile gloves"),
    ("Surgical suture", "Surgical suture"),
    ("Bladder catheterization set", "Bladder catheterization set"),
    ("Gastric lavage set", "Gastric lavage set"),
    ("Waste bags", "Waste bags"),
    ("Alcohol swabs", "Alcohol swabs"),
    ("Emergency Blanket NRC", "Emergency Blanket NRC"),
    ("Tactical tourniquet", "Tactical tourniquet"),
    ("Cervical collar", "Cervical collar"),
    ("SAM Splint", "SAM Splint"),
]

DRESSING_EQUIPMENT = [
    ("Gauze - single", "Gauze - single"),
    ("Chest seal", "Chest seal"),
    ("Hydrogel", "Hydrogel"),
    ("Gauze", "Gauze"),
    ("Elastic bandage", "Elastic bandage"),
    ("Knitted bandage", "Knitted bandage"),
    ("Plaster for wound", "Plaster for wound"),
    ("Adhesive tape", "Adhesive tape"),
    ("Triangular bandage", "Triangular bandage"),
    ("Codofix", "Codofix"),
]

REUSABLE_EQUIPMENT = [
    ("Medical tourniquet", "Medical tourniquet"),
    ("Stethoscope", "Stethoscope"),
    ("Pressure gauge", "Pressure gauge"),
    ("Pulse oximeter", "Pulse oximeter"),
    ("Thermometer", "Thermometer"),
    ("Diagnostic flashlight", "Diagnostic flashlight"),
    ("Glucometer", "Glucometer"),
    ("Laryngoscope", "Laryngoscope"),
    ("Laryngoscope blade", "Laryngoscope blade"),
    ("Protection glasses", "Protection glasses"),
    ("Magill forceps", "Magill forceps"),
    ("Electric suction", "Electric suction"),
    ("Manual suction", "Manual suction"),
    ("Oxygen tank", "Oxygen tank"),
    ("Oxygen reducer", "Oxygen reducer"),
    ("PEEP valve", "PEEP valve"),
    ("Resuscitator", "Resuscitator"),
    ("Respirator", "Respirator"),
    ("Document pad", "Document pad"),
    ("MCR card", "MCR card"),
    ("Paramedic card", "Paramedic card"),
    ("Heart monitor", "Heart monitor"),
    ("Forceps", "Forceps"),
    ("Defibrillator", "Defibrillator"),
    ("AED", "AED"),
    ("Capnometer", "Capnometer"),
    ("Scissors", "Scissors"),
]

MEDICAL_EQUIPMENT_NAME_CHOICES = [
    ("Drugs", DRUGS),
    ("Disposable", DISPOSABLE_EQUIPMENT),
    ("Reusable", REUSABLE_EQUIPMENT),
    ("Dressing", DRESSING_EQUIPMENT),
]

MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES = [
    ("Durable", "Durable"),
    ("Disposable", "Disposable"),
    ("Electronic", "Electronic"),
]

CONTAINER_NAME_CHOICES = [
    ("Main warehouse", "Main warehouse"),
    ("Trauma Wall - ALS", "Trauma Wall - ALS"),
    ("Trauma Wall - hospital", "Trauma Wall - hospital"),
    ("Backpack - ALS", "Backpack - ALS"),
    ("Backpack - ALS Ampoule", "Backpack - ALS Ampoule"),
    ("Backpack - R1", "Backpack - R1"),
    ("Bag - R1", "Bag - R1"),
    ("Trunk - ALS", "Trunk - ALS"),
    ("Trunk - ALS Ampoule", "Trunk - ALS Ampoule"),
    ("Storage Drawer - hospital", "Storage Drawer - hospital"),
]

DRUG_ACTIVE_SUBSTANCES = sorted(
    [
        ("Acidum acetylsalicylicum", "Acidum acetylsalicylicum"),
        ("Ketoprofenum", "Ketoprofenum"),
        ("Ibuprofenum", "Ibuprofenum"),
        ("Metamizolum natricum", "Metamizolum natricum"),
        ("Paracetamolum", "Paracetamolum"),
        ("Morphini sulfas", "Morphini sulfas"),
        ("Fentanylum", "Fentanylum"),
        ("Naloxoni hydrochloridum", "Naloxoni hydrochloridum"),
        ("Budesonidum", "Budesonidum"),
        ("Hydrocortisonum", "Hydrocortisonum"),
        # 10
        ("Dexamethasoni phosphas", "Dexamethasoni phosphas"),
        ("Diazepamum", "Diazepamum"),
        ("Clonazepam", "Clonazepam"),
        ("Midazolamum", "Midazolamum"),
        ("Flumazenilum", "Flumazenilum"),
        ("Atropini sulfas", "Atropini sulfas"),
        ("Adenosinum", "Adenosinum"),
        ("Amiodaroni hydrochloridum", "Amiodaroni hydrochloridum"),
        ("Lidocaini hydrochloridum", "Lidocaini hydrochloridum"),
        ("Epinephrinum", "Epinephrinum"),
        # 20
        ("Salbutamolum", "Salbutamolum"),
        ("Urapidilum", "Urapidilum"),
        ("Metoprololi tartras", "Metoprololi tartras"),
        ("Drotaverini hydrochloridum ", "Drotaverini hydrochloridum "),
        ("Glyceroli trinitras", "Glyceroli trinitras"),
        ("Clopidogrelum", "Clopidogrelum"),
        ("Ticagrelor", "Ticagrelor"),
        ("Hepariunum natricum", "Hepariunum natricum"),
        ("Thiethylperazinum", "Thiethylperazinum"),
        ("Metoclopramidum", "Metoclopramidum"),
        # 30
        ("Furosemidum", "Furosemidum"),
        ("Mannitolum", "Mannitolum"),
        ("Hydroxyzinum", "Hydroxyzinum"),
        ("Magnesii sulfas", "Magnesii sulfas"),
        ("Clemastinum", "Clemastinum"),
        ("Natrii hydrogenocarbonas 8,4%", "Natrii hydrogenocarbonas 8,4%"),
        ("Captoprilum", "Captoprilum"),
        ("Glucagoni hydrochloridum", "Glucagoni hydrochloridum"),
        ("Glukoza 20%", "Glukoza 20%"),
        ("Glukoza 40%", "Glukoza 40%"),
        # 40
        ("Glukoza 5%", "Glukoza 5%"),
        ("Natrii chloridum 0,9%", "Natrii chloridum 0,9%"),
        ("Optilyte", "Optilyte"),
        ("Solutio Ringeri", "Solutio Ringeri"),
        ("Plasmalyte", "Plasmalyte"),
        ("Acidum tranexamicum", "Acidum tranexamicum"),
        ("Polstigminum", "Polstigminum"),
        ("Ondansetronum", "Ondansetronum"),
        ("Hyoscini butylbromidum", "Hyoscini butylbromidum"),
        ("Suxamethonii chloridum", "Suxamethonii chloridum"),
        # 50
        ("Calcii chloridum dihydricum", "Calcii chloridum dihydricum"),
        ("Propofolum", "Propofolum"),
        ("Pantoprazolum", "Pantoprazolum"),
        ("Aqua pro injectione", "Aqua pro injectione"),
        ("Nitrendipinum", "Nitrendipinum"),
        ("Rocuronium", "Rocuronium"),
        ("Ketamine hydrochloride", "Ketamine hydrochloride"),
    ]
)
DRUG_DOSAGE_FORM = [
    ("Pills", "Pills"),
    ("Nebulizer", "Nebulizer"),
    ("Injection", "Injection"),
    ("Ointment", "Ointment"),
    ("Areosol", "Areosol"),
    ("Rectal enema", "Rectal enema"),
]

FLUID_VOLUME = [
    ("5ml", "5ml"),
    ("10ml", "10ml"),
    ("20ml", "20ml"),
    ("50ml", "50ml"),
    ("100ml", "100ml"),
    ("250ml", "250ml"),
    ("500ml", "500ml"),
    ("1000ml", "1000ml"),
]

CANNULA_SIZE = [
    ("Purple - 26G", "Purple - 26G"),
    ("Yellow - 24G", "Yellow - 24G"),
    ("Blue - 22G", "Blue - 22G"),
    ("Pink - 20G", "Pink - 20G"),
    ("Green - 18G", "Green - 18G"),
    ("White - 17G", "White - 17G"),
    ("Gray - 16G", "Gray - 16G"),
    ("Orange - 14G", "Orange - 14G"),
]

NEEDLE_SIZE = [
    ("Orange - 0.5mm", "Orange - 0.5mm"),
    ("Blue - 0.6mm", "Blue - 0.6mm"),
    ("Black - 0.7mm", "Black - 0.7mm"),
    ("Green - 0.8mm", "Green - 0.8mm"),
    ("Yellow - 0.9mm", "Yellow - 0.9mm"),
    ("Beige - 1.1mm", "Beige - 1.1mm"),
    ("Pink - 1.2mm", "Pink - 1.2mm"),
]

SYRINGE_VOLUME = [
    ("1ml", "1ml"),
    ("2ml", "2ml"),
    ("5ml", "5ml"),
    ("10ml", "10ml"),
    ("20ml", "20ml"),
    ("50ml", "50ml"),
    ("100ml", "100ml"),
]

BIG_SIZE = [("Red - child", "Red - child"), ("Blue - adult", "Blue - adult")]

LT_TUBE_SIZE = [
    ("Clear #0", "Clear #0"),
    ("White #1", "White #1"),
    ("Green #2", "Green #2"),
    ("Orange #2.5", "Orange #2.5"),
    ("Yellow #3", "Yellow #3"),
    ("Red #4", "Red #4"),
    ("Purple #5", "Purple #5"),
]

GLOVES_SIZE = [("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")]

STERILE_GLOVES_SIZE = [
    ("6.0", "6.0"),
    ("6.5", "6.5"),
    ("7.0", "7.0"),
    ("7.5", "7.5"),
    ("8.0", "8.0"),
    ("8.5", "8.5"),
    ("9.0", "9.0"),
]

GAUZE_SIZE = [("1/4m^2", "1/4m^2"), ("1/2m^2", "1/2m^2"), ("1m^2", "1m^2")]

NPA_TUBE_SIZE = [
    ("5.0", "5.0"),
    ("5.5", "5.5"),
    ("6.0", "6.0"),
    ("6.5", "6.5"),
    ("7.0", "7.0"),
    ("7.5", "7.5"),
    ("8.0", "8.0"),
    ("8.5", "8.5"),
    ("9.0", "9.0"),
    ("9.5", "9.5"),
]

OPA_TUBE_SIZE = [
    ("000", "000"),
    ("00", "00"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
]

ET_TUBE_SIZE = [
    ("2.5", "2.5"),
    ("3.0", "3.0"),
    ("3.5", "3.5"),
    ("4.0", "4.0"),
    ("4.5", "4.5"),
    ("5.0", "5.0"),
    ("5.5", "5.5"),
    ("6.0", "6.0"),
    ("6.5", "6.5"),
    ("7.0", "7.0"),
    ("7.5", "7.5"),
    ("8.0", "8.0"),
    ("8.5", "8.5"),
    ("9.0", "9.0"),
    ("9.5", "9.5"),
    ("10.0", "10.0"),
]

BLADE_SIZE = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]

O2_MASK_TYPE = [
    ("Nasal cannula", "Nasal cannula"),
    ("Simple mask", "Simple mask"),
    ("Reservoir mask", "Reservoir mask"),
]
O2_MASK_SIZE = [("Child", "Child"), ("Adult", "Adult")]

VENTILATION_MASK_SIZE = [("Child", "Child"), ("Adult", "Adult")]
