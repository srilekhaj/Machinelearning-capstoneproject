from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=cpredModel
        fields=['age', 'bmi','children','sex_male', 'smoker_yes', 'region_southeast']
