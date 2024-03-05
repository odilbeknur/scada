from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from django.db.models import Q
import django_crontab
from django.http import HttpResponse
import requests

def my_cron_job():
        
        url = f'http://10.40.9.25:8001/watering/1?water=200'
        
        response = requests.post(url)
        print(url)
        print(response.status_code)

        if response.status_code == 200:
            print("Plant watered successfully")
        else:
            print("Error watering plant")