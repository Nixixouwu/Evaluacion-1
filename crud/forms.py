from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'