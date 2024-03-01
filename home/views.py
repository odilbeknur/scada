from django.shortcuts import render
from django.views.generic import ListView
from .models import Category,Plant,Watering
from django.db.models import Count
from django.db.models import Q

from django.http import HttpResponse
import requests

def names(request):
    #pull data from third party rest api
    response = requests.get('http://10.40.9.25:8001/api/v2/get/all/plant')
    #convert reponse data into json
    names = response.json()
    #print(names)
    return render(request, "api.html", {'names': names})
    pass

def watering(request):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'admin/category-create.html'
    login_url = 'login'
    success_url = reverse_lazy('category-create')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    r
#http://10.40.9.25:8001/watering/{{name_p}}?{{name}}

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
