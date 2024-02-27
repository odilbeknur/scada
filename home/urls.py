from django.urls import path
from .views import Home, Base, Detail, SearchResultsView
from . import views

urlpatterns = [
    path('', Home, name='home'),
   # path('', views.names, name = 'name'),
    path('base/<int:pk>', Base, name='base'),
    path('base/<int:pk>/detail', Detail, name='detail'),
    path('search', SearchResultsView.as_view(), name='search'),
]