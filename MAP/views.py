from rest_framework.views import APIView
from rest_framework.response import Response

class ListView(APIView):
    def get(self, request):
        return Response(
            {
                "leaflet a": "https://mapsleaflet.vercel.app/leaflet/a",
                "leaflet b": "https://mapsleaflet.vercel.app/leaflet/b",
                "leaflet c": "https://mapsleaflet.vercel.app/leaflet/c",
                "leaflet d": "https://mapsleaflet.vercel.app/leaflet/d",
                "leaflet e": "https://mapsleaflet.vercel.app/leaflet/e",
                "leaflet f": "https://mapsleaflet.vercel.app/leaflet/f",
                "leaflet g": "https://mapsleaflet.vercel.app/leaflet/g",
                "leaflet h": "https://mapsleaflet.vercel.app/leaflet/h",
                "leaflet i": "https://mapsleaflet.vercel.app/leaflet/i",
                "leaflet j": "https://mapsleaflet.vercel.app/leaflet/j",
                "leaflet k": "https://mapsleaflet.vercel.app/leaflet/k",
            }
        )
