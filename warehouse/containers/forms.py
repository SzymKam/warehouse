from django.forms import ModelForm, inlineformset_factory
from .models import Container, MedicalEquipment, Drug


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
    class Meta:
        model = MedicalEquipment
        fields = "__all__"


DrugFormset = inlineformset_factory(MedicalEquipment, Drug, fields="__all__")
