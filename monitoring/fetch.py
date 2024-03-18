import requests
from .models import Report
import django_crontab

def fetch_to_report():
    url = "http://10.40.9.25:8001/api/v2/get/all/plant"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Iterate over plant data and create Report objects
        for plant_data in data:
            plant_name = plant_data.get('plant_name')
            soil_value = plant_data.get('soil_value')
            soilpin_num = plant_data.get('soilpin_num')
            soilpin_status = plant_data.get('soilpin_status')
            pump_pin = plant_data.get('pump_pin')
            pump_status = plant_data.get('pump_status')
            
            # Save data to Report model
            Report.objects.create(
                plant_name=plant_name,
                soil_value=soil_value,
                soilpin_num=soilpin_num,
                soilpin_status=soilpin_status,
                pump_pin=pump_pin,
                pump_status=pump_status
            )
            
        return True  # Data fetched and saved successfully
        
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return False  # Error occurred while fetching or saving data
