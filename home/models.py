from django.db import models
from io import BytesIO
from django.core.files import File


class Room(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images', null=True)
    def __str__(self) -> str:
        return self.name



class Responsible(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.TextField(null=True)
    image = models.ImageField(upload_to='static/images', null=True)


    def __str__(self) -> str:
        return self.fullname

class Plant(models.Model):
    plant_room = models.ForeignKey(Room, related_name='category', on_delete=models.PROTECT, blank=True)
    plant_name = models.CharField(max_length=70, blank=True)
    plant_image = models.ImageField(upload_to='static/images', null=True)
    plant_num = models.CharField(max_length=70, blank=True)
    capacity = models.CharField(max_length=70, blank=True)

    soil_value = models.CharField(max_length=70, blank=True)
    soilpin_num =  models.CharField(max_length=70, blank=True)
    soilpin_status =  models.CharField(max_length=70, null=True, default='False')
    
    pump_pin = models.CharField(max_length=70, blank=True)
    pump_status = models.CharField(max_length=70, null=True, default='False')

    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.plant_name)

class Watering(models.Model):
    plant_id = models.CharField(max_length=100)
    w_status = models.BooleanField()

    def __str__(self) -> str:
        return self.w_status

class Logs(models.Model):
    artist = models.ForeignKey(Plant, on_delete=models.CASCADE)
    status = models.BooleanField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()        