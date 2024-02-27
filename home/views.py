from django.shortcuts import render
from django.views.generic import ListView
from .models import Category,Plant
from django.db.models import Count
from django.db.models import Q

from django.http import HttpResponse
import requests

def names(request):
    #pull data from third party rest api
    response = requests.get('http://192.168.100.13:8000/api/v2/get/all/plant')
    #convert reponse data into json
    names = response.json()
    #print(names)
    return render(request, "api.html", {'names': names})
    pass

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
