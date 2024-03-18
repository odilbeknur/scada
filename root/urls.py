from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import Admin_index, Admin_plant, Admin_device, RoomCreateView, baseview, PlantCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ResponsibleCreateView
from . import views

urlpatterns = [
    path('admin-index/', Admin_index, name='admin-index'),
    path('watering/', views.water, name='watering'),
    path('admin-plants/', Admin_plant, name='admin-plants'),
    path('admin-devices/', Admin_device, name='admin-devices'),
    path('admin-index/room-create', RoomCreateView.as_view(), name='room-create'),  
    path('admin-index/poka-base/<int:pk>', baseview, name='base-view'),
    path('admin-index/add-plant', PlantCreateView.as_view(), name='plant-create'),
    path('admin-index/poka-base/<int:pk>/admin-detail-of-product', ProductDetailView, name='product-detail'),
    path('admin-index/poka-base/<int:pk>/product-update', ProductUpdateView, name='product-update'),
    path('admin-index/poka-base/<int:pk>/product-delete', ProductDeleteView, name='product-delete'),
    path('admin-index/responsible-create', ResponsibleCreateView.as_view(), name='responsible-create'),
    #path('admin-index/model-create', ModelCreateView.as_view(), name='model-create'),
    #path('admin/search', SearchResultsView.as_view(), name='admin-search'),
]