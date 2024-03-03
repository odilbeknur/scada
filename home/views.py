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
    pass

def water(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Get data from the form
            water = form.cleaned_data['name_p']
            water = form.cleaned_data['amount']
            # Convert the status to lowercase for consistency
            status = status.lower()
            # Construct the URL based on the form input
            url = f'http://10.40.9.25:8001/watering/{name_p}?{amount}'
            
            # Send POST request to FastAPI
            payload = {'status': status}  # Adjust payload as per your FastAPI endpoint
            response = requests.post(url, json=payload)

            # Handle response
            if response.status_code == 200:
                # Request successful
                return render(request, 'api.html')
            else:
                # Request failed
                return render(request, 'error.html')
    else:
        form = MyForm()

    return render(request, 'api.html', {'form': form})

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
