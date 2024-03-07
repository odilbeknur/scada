from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django import forms
from home.models import Category, Plant, Responsible
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CategoryCreateForm, PlantCreateForm, ProductUpdateForm, ResponsibleCreateForm, ProductDetailUpdateForm
import random
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

def Admin_index(request):
    categories = Plant.objects.annotate(count=Count('plant_num'))
    return render(request, 'admin/admin-index.html', {'queryset': categories})

def Admin_plants(request):
    plants = Plant.objects.annotate(count=Count('plant_num'))
    return render(request, 'admin/admin-plants.html', {'queryset': plants})



def water(request):
    if request.method == 'POST':
        # Process form data and send POST request to FastAPI as before
        
        if response.status_code == 200:
            return JsonResponse({'success': True})  # Return JSON response indicating success
        else:
            return JsonResponse({'success': False})  # Return JSON response indicating failure
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  # Return JSON response for invalid method



class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'admin/category-create.html'
    login_url = 'login'
    success_url = reverse_lazy('category-create')
    success_message = "Комната успешно добавлена"

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Error: {e}')
            return self.form_invalid(form)


class ResponsibleCreateView(LoginRequiredMixin, CreateView):
    model = Responsible
    form_class = ResponsibleCreateForm
    template_name = 'admin/responsible-create.html'
    login_url = 'login'
    success_url = reverse_lazy('responsible-create')
    success_message = "Ответственный успешно добавлен"

    def form_valid(self, form):
         form.instance.author = self.request.user
         try:
                return super().form_valid(form)
         except Exception as e:
                messages.error(self.request, f'Error: {e}')
                return self.form_invalid(form)




def baseview(request, pk):
    query = Plant.objects.filter(category_id__id=pk)
    get_cat = Category.objects.filter(id=pk)
    return render(request, 'admin/admin-base.html', {'query': query, 'get_cat': get_cat})

class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'admin/plant-create.html'
    login_url = 'login'
    success_url = reverse_lazy('plant-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant_room'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)     


def ProductDetailView(request, pk):
    query = Plant.objects.filter(id=pk)
    eq = get_object_or_404(Plant, pk=pk)
    form = ProductDetailUpdateForm(request.POST or None, instance=eq)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product-detail', pk=eq.pk)
    return render(request, 'admin/admin-detail.html', {'query': query, 'form': form})

def ProductUpdateView(request, pk):
    equipment = get_object_or_404(Plant, pk=pk)
    red = equipment.category_id.id
    form = ProductUpdateForm(request.POST or None, instance=equipment)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('base-view', pk=red)
    return render(request, 'admin/admin-product-update.html', {'form': form})
    
def ProductDeleteView(request, pk):
    query = Plant.objects.get(pk=pk)
    red = query.category_id.id
    if request:
        query.delete()
        return redirect('base-view', pk=red)
    return render(request, 'admin/admin-base.html')

