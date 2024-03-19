from django.urls import path
from .views import Home, Base, Detail, SearchResultsView
from . import views

urlpatterns = [
    path('', Home, name='home'),
    path('api', views.names, name = 'name'),
    path('watering/', views.water, name='watering'),
    path('report/', views.fetch_to_report, name='report'),
    path('base/<int:pk>', Base, name='base'),
    path('base/<int:pk>/detail', Detail, name='detail'),
    path('search', SearchResultsView.as_view(), name='search'),
]
