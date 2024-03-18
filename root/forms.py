from dataclasses import fields
from django import forms
from home.models import Room, Plant, Responsible
from django.core.exceptions import ValidationError
from django.utils.safestring import SafeString

class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'image']
        labels = {
            'name': 'Категория',
            'image': 'Категория (фото)',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
position_choices = (
        ('', 'Выберите должность'),
        ('Тех.персонал', 'Тех.персонал'),
        ('Ведущий специалист', 'Ведущий специалист'),
        ('Главный специалист', 'Главный специалист'),
    )         

class ResponsibleCreateForm(forms.ModelForm):
    position = forms.ChoiceField(choices=position_choices)
    class Meta:
        model = Responsible
        fields = ['fullname', 'position', 'image']
        labels = {
            'fullname': 'Ф.И.О. ответственного',
            'position':'Должность',
            'image': 'Фото'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.initial['position'] = ''


status_choices = (
       ('True', 'В сети'),
       ('False', 'Не в сети'),
    )    

class PlantCreateForm(forms.ModelForm):
    plant_room = forms.ModelChoiceField(queryset=Room.objects.all(), label='Комната', widget=forms.Select(attrs={'class': "form-floating form-floating-outline mb-4"}))
    soilpin_status = forms.ChoiceField(choices=status_choices)
    pump_status = forms.ChoiceField(choices=status_choices)
    
    class Meta:
        model = Plant
        fields = ['plant_room','plant_name','plant_image','plant_num', 'capacity', 'soil_value', 'soilpin_num', 'soilpin_status', 'pump_pin', 'pump_status', 'description']
       
        labels = {
            'plant_room': 'Комната',
            'plant_name': 'Название',
            'plant_image': 'Загрузите изображение',
            'plant_num': 'ID номер',
            'capacity': 'Объем',
            'soil_value': 'Влажность',
            'soilpin_num': 'Датчик влажности (pin)',
            'soilpin_status': 'Датчик влажности (статус)',
            'pump_pin': 'Насос (pin)',
            'pump_status': 'Насос (статус)',
            'description': 'Описание',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        
        




class ProductUpdateForm(forms.ModelForm):
    category_id = forms.ModelChoiceField( queryset=Room.objects.all(), label='Категория', widget=forms.Select(attrs={'class': "form-control"}))
    room_number = forms.ChoiceField(choices=((str(x), x) for x in range(150,540)), label='Объект', widget=forms.Select(attrs={'class': "form-control"}))
    #model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Модель устройства', widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.all(), label='Ответственный', widget=forms.Select(attrs={'class': "form-control"}))
    processor = forms.CharField(max_length=70, label='Процессор', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    memory = forms.CharField(max_length=70, label='Память', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    mac_address = forms.CharField(max_length=50, label='MAC-адрес', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    ip_address = forms.CharField(max_length=50, label='IP-адрес', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    position = forms.CharField(label='Коментарии', widget=forms.Textarea(attrs={'class': "form-control"}))
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