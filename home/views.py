from django.shortcuts import render
from django.views.generic import ListView
from .models import Room,Plant,Watering
from django.db.models import Count
from django.db.models import Q
import django_crontab
from django.http import HttpResponse
import requests
from django import forms


from .forms import MyForm



def names(request):
    #pull data from third party rest api
    response = requests.get('http://10.40.9.25:8001/api/v2/get/all/plant')
    #response = requests.get('http://70.70.0.68:8001/api/v2/get/all/plant')

    #convert reponse data into json
    names = response.json()
    #print(names)
    return render(request, "api.html", {'names': names})


from django.http import JsonResponse


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
                return JsonResponse({'success': True})  # Return JSON response indicating success
            else:
                return JsonResponse({'success': False})  # Return JSON response indicating failure
    else:
        form = MyForm()

    return render(request, 'api.html', {'form': form})
# cron.py

   


def Home(request):
    query = Room.objects.annotate(count=Count('category'))
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
