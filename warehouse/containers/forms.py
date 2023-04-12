from django.forms import ModelForm, inlineformset_factory, modelformset_factory
from .models import Container, MedicalEquipment, Drug, BaseMedicalEquipment


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


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = "__all__"
