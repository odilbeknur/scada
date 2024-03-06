from django.db import models
from io import BytesIO
from django.core.files import File


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/rooms')

    def __str__(self) -> str:
        return self.name

    
class Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Responsible(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.TextField(max_length=100, blank=True)    
    image = models.ImageField(upload_to='static/images/responsible', null=True)

    def __str__(self) -> str:
        return self.fullname

class Plant(models.Model):
    platn_room = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT, blank=True)
    plant_name = models.CharField(max_length=70, blank=True)
    plant_image = models.ImageField(upload_to='static/images/plants', null=True)
    plant_num = models.CharField(max_length=70, blank=True)
    capacity = models.CharField(max_length=70, blank=True)

    soil_value = models.CharField(max_length=70, blank=True)
    soilpin_num =  models.CharField(max_length=70, blank=True)
    soilpin_status =  models.CharField(max_length=70, null=True, default='Не в сети')
    
    pomp_pin = models.CharField(max_length=70, blank=True)
    pomp_status = models.CharField(max_length=70, null=True, default='Не в сети')

    description = models.TextField()

    def __str__(self) -> str:
        return str(self.plant_num)

class Watering(models.Model):
    plant_id = models.CharField(max_length=100)
    w_status = models.BooleanField()

    def __str__(self) -> str:
        return self.name