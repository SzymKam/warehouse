import inspect
from typing import Type

from django.forms import modelformset_factory, ModelForm, BaseModelFormSet
from django.forms.widgets import DateInput

from containers import models


class ContainerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        excluded_choice = "Main warehouse"
        if excluded_choice in dict(self.fields["name"].choices):
            choices = list(self.fields["name"].choices)
            choices.remove((excluded_choice, excluded_choice))
            self.fields["name"].choices = choices

    class Meta:
        model = models.Container
        fields = "__all__"


def create_forms() -> dict[str, Type[BaseModelFormSet]]:
    widgets = {"expiration_date": DateInput(attrs={"type": "date"})}
    model_classes = [cls for name, cls in inspect.getmembers(models, inspect.isclass)]
    forms = {}
    for model_class in model_classes:
        form_class = modelformset_factory(
            model_class, fields="__all__", widgets=widgets
        )
        form_name = f"{model_class.__name__}Form"
        forms[form_name] = form_class
    return forms
