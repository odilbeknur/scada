from django.db import models
from home.models import Plant

# Create your models here.
class Alert(models.Model):
     LEVEL_CHOICES = [
         ('LOW', 'Low'),
         ('MEDIUM', 'Medium'),
         ('HIGH', 'High'),
     ]

     message = models.TextField()
     level = models.CharField(max_length = 10, choices = LEVEL_CHOICES)
     timestamp = models.DateTimeField(auto_now_add = True)
     def __str__(self):
        return f"{self.get_level_display()}: {self.message}"

class Report(models.Model):

    plant_name = models.ForeignKey(Plant, related_name='category', on_delete=models.PROTECT, blank=True)
    soil_value = models.CharField(max_length=70, blank=True)
    soilpin_num = models.CharField(max_length=70, blank=True)
    soilpin_status = models.CharField(max_length=70, blank=True, default='False')
    pump_pin = models.CharField(max_length=70, blank=True)
    pump_status = models.CharField(max_length=70, blank=True, default='False')

    def __str__(self):
            return self.plant_name
