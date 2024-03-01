from dataclasses import fields
from django import forms
from home.models import Category, Model, Plant, Responsible
from django.core.exceptions import ValidationError
import requests

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
        labels = {
            'name': 'Категория',
            'image': 'Категория (фото)',
        }
def watering(request):
    #pull data from third party rest api
    response = requests.get('http://10.40.9.25:8001/api/v2/get/all/plant')
    #convert reponse data into json
    names = response.json()
    #print(names)
    return render(request, "api.html", {'names': names})
    pass

