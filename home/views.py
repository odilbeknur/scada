from django.shortcuts import render
from django.views.generic import ListView
from .models import Category,Plant,Watering
from django.db.models import Count
from django.db.models import Q

from django.http import HttpResponse
import requests

from .forms import MyForm

def names(request):
    #pull data from third party rest api
    response = requests.get('http://10.40.9.25:8001/api/v2/get/all/plant')
    #convert reponse data into json
    names = response.json()
    #print(names)
    return render(request, "api.html", {'names': names})
    pwater

from django.shortcuts import render
from django import forms
import requests

def water(request):
    if request.method == 'POST':
        class MyForm(forms.Form):
            plant = forms.CharField(max_length=100)
            amount = forms.IntegerField()
        
        form = MyForm(request.POST)
        if form.is_valid():
            # Get data from the form
            plant = form.cleaned_data['plant']
            amount = form.cleaned_data['amount']
            
            # Construct the URL based on the form input
            url = f'http://10.40.9.25:8001/watering/{plant}?water={amount}'
            
            # Send POST request to FastAPI
            response = requests.post(url)
            print(url)
            print(response.status_code)

            # Handle response
            if response.status_code == 200:
                # Request successful
                return render(request, 'api.html')
            else:
                # Request failed
                return render(request, 'error.html')
    else:
        form = MyForm()

    return render(request, 'water_form.html', {'form': form})
# cron.py

from django_cron import CronJobBase, Schedule
from .forms import MyForm  # Import your form class here
import requests


class WaterPlantCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Run every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.water_plant_cron_job'  # A unique code for your cron job

    def do(self):
        # Your watering logic goes here
        plant = 'plant_name'  # Replace with the actual plant name
        amount = 10  # Replace with the amount to water
        url = f'http://10.40.9.25:8001/watering/{plant}?water={amount}'
        
        response = requests.post(url)
        print(url)
        print(response.status_code)

        if response.status_code == 200:
            print("Plant watered successfully")
        else:
            print("Error watering plant")


def Home(request):
    query = Category.objects.annotate(count=Count('category'))
    return render(request, 'index.html', {'query': query})

def Base(request, pk):
    query =Plant.objects.filter(category_id__id=pk)
    return render(request, 'base.html', {'query': query})


def Detail(request, pk):
    query =Plant.objects.filter(pk=pk)
    return render(request, 'detail.html', {'query': query})
    
class SearchResultsView(ListView):
    model =Plant
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list =Plant.objects.filter(
            Q(inventar_number__icontains=query)
        )
        return object_list

def WateringView(request, pk):
    query = Plant.objects.filter(id=pk)
    eq = get_object_or_404(Plant, pk=pk)
    form = ProductDetailUpdateForm(request.POST or None, instance=eq)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product-detail', pk=eq.pk)
    return render(request, 'admin/admin-detail.html', {'query': query, 'form': form})
