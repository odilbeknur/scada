from dataclasses import fields
from django import forms
from home.models import Category, Plant, Responsible
from django.core.exceptions import ValidationError

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
        labels = {
            'name': 'Категория',
            'image': 'Категория (фото)',
        }

class ResponsibleCreateForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ['fullname', 'description']
        labels = {
            'fullname': 'Ф.И.О. ответственного',
            'description':'Должность',
        }


class PlantCreateForm(forms.ModelForm):
    plant_room = forms.ModelChoiceField(queryset=Category.objects.all(), label='Комната', widget=forms.Select(attrs={'class': "form-select"}))


    class Meta:
        model = Plant
        fields = ['plant_room','plant_name','plant_num', 'capacity', 'soil_value', 'soilpin_num', 'soilpin_status', 'pomp_pin', 'pomp_status', 'description']
        labels = {
            'plant_room': 'Комната',
            'plant_name': 'Название',
            'plant_num': 'ID номер',
            'capacity': 'Объем',
            'soil_value': 'Влажность',
            'soilpin_num': 'Датчик влажности (pin)',
            'soilpin_status': 'Датчик влажности (статус)',
            'pomp_pin': 'Насос (pin)',
            'pomp_status': 'Насос (статус)',
            'description': 'Описание',
        }

status_choices = (
        ('В сети', 'В сети'),
        ('Не в сети', 'Не в сети'),
        ('Не подключен', 'Не подключен'),
    )


class ProductUpdateForm(forms.ModelForm):
    category_id = forms.ModelChoiceField( queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={'class': "form-control"}))
    room_number = forms.ChoiceField(choices=((str(x), x) for x in range(150,540)), label='Объект', widget=forms.Select(attrs={'class': "form-control"}))
    #model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Модель устройства', widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.all(), label='Ответственный', widget=forms.Select(attrs={'class': "form-control"}))
    processor = forms.CharField(max_length=70, label='Процессор', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    memory = forms.CharField(max_length=70, label='Память', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    mac_address = forms.CharField(max_length=50, label='MAC-адрес', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    ip_address = forms.CharField(max_length=50, label='IP-адрес', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Коментарии', widget=forms.Textarea(attrs={'class': "form-control"}))
    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
            model = Plant
            exclude = ('inventar_number', 'qr_code',)

class ProductDetailUpdateForm(forms.ModelForm):
    status_choices = (
        ('В сети', 'В сети'),
        ('Не в сети', 'Не в сети'),
        ('Не подключен', 'Не подключен'),
    )
    status = forms.ChoiceField(choices=status_choices, label='', widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = Plant
        fields = ['status']