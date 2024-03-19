from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from django.db.models import Q
import django_crontab
from django.http import HttpResponse
import requests
from monitoring.models import Report

def my_cron_job():
        
        url = f'http://10.40.9.25:8001/watering/1?water=200'
        
        response = requests.post(url)
        print(url)
        print(response.status_code)

        if response.status_code == 200:
            print("Plant watered successfully")
        else:
            print("Error watering plant")

def fetch_to_report(request):
    url = "http://70.70.0.68:8000/api/v2/get/all/plant"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Iterate over plant data and create Report objects
        for plant_data in data:
            name = plant_data.get('name')
            soil_value = plant_data['pin_soil']['pin_value']
            soilpin_num = plant_data['pin_soil']['pin_num']
            soilpin_status = plant_data['pin_soil']['pin_state']
            pump_pin = plant_data['pin_pomp']['pin_value']
            pump_status = plant_data['pin_pomp']['pin_num']
            
            # Save data to Report model
            Report.objects.create(
                name=name,
                soil_value=soil_value,
                soilpin_num=soilpin_num,
                soilpin_status=soilpin_status,
                pump_pin=pump_pin,
                pump_status=pump_status
            )
        return HttpResponse("Data fetched and saved successfully")
        
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse("Failed to fetch or save data", status=500)

