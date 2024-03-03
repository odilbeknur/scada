from dataclasses import fields
from django import forms
from home.models import Category, Model, Plant, Responsible
from django.core.exceptions import ValidationError
import requests

class MyForm(forms.Form):
    STATUS_CHOICES = (
        ('true', 'True'),
        ('false', 'False'),
    )
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)

