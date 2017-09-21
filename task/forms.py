from django import forms
from .models import *


# Форма модели Data
class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        exclude = [""]