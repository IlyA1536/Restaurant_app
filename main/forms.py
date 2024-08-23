from django import forms
from menu.models import Dish

class ManageRecommendedDishesForm(forms.Form):
    recommended_dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', None)
        super().__init__(*args, **kwargs)
        self.fields['recommended_dishes'].queryset = Dish.objects.all().order_by('name')
        if initial is not None:
            self.fields['recommended_dishes'].initial = initial
