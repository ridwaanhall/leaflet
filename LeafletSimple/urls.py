from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.LeafletAView.as_view(), name='leaflet-a'),
    path('b/', views.LeafletBView.as_view(), name='leaflet-b'),
]