from django.views.generic import TemplateView

class LeafletView(TemplateView):
    template_name = 'LeafletSimple/leaflet.html'