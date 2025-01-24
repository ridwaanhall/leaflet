from django.views.generic import TemplateView

views = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o',
    'p',
]

for view in views:
    globals()[f'Leaflet{view.upper()}View'] = type(
        f'Leaflet{view.upper()}View',
        (TemplateView,),
        {'template_name': f'LeafletSimple/{view}.html'}
    )
