from django.views.generic import TemplateView

class LeafletAView(TemplateView):
    template_name = 'LeafletSimple/leaflet-a.html'
    
class LeafletBView(TemplateView):
    template_name = 'LeafletSimple/leaflet-b.html'
    
class LeafletCView(TemplateView):
    template_name = 'LeafletSimple/leaflet-c.html'