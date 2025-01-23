from django.urls import path
from . import views

urlpatterns = [
    path(f'{view}/', getattr(views, f'Leaflet{view.upper()}View').as_view(), name=f'leaflet_{view}')
    for view in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
]
