from django.forms import ModelForm, inlineformset_factory, modelformset_factory
from .models import Container, MedicalEquipment, Drug, BaseMedicalEquipment, NameModel


class ContainerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        excluded_choice = "Main warehouse"
        if excluded_choice in dict(self.fields["name"].choices):
            choices = list(self.fields["name"].choices)
            choices.remove((excluded_choice, excluded_choice))
            self.fields["name"].choices = choices

    class Meta:
        model = Container
        fields = "__all__"


class MedicalEquipmentForm(ModelForm):
    """simple way to add base equipment"""

    class Meta:
        model = MedicalEquipment
        fields = "__all__"


# """here i want to create form to expand for specific models. Create base with only name, and formest with
# additional information"""
class EquipmentNameForm(ModelForm):
    class Meta:
        model = NameModel
        fields = "__all__"


class BaseMedicalEquipmentForm(ModelForm):
    class Meta:
        model = BaseMedicalEquipment
        fields = "__all__"


DrugFormset = modelformset_factory(Drug, fields="__all__", extra=1)
MedicalEquipmentFormset = modelformset_factory(
    MedicalEquipment, fields="__all__", extra=1
)
