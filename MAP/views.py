from rest_framework.views import APIView
from rest_framework.response import Response

class ListView(APIView):
    def get(self, request):
        return Response(
            {
                "leaflet a": "/a",
                "leaflet b": "/b",
                "leaflet c": "/c",
                "leaflet d": "/d",
                "leaflet e": "/e",
                "leaflet f": "/f",
                "leaflet g": "/g",
                "leaflet h": "/h",
                "leaflet i": "/i",
                "leaflet j": "/j",
                "leaflet k": "/k",
            }
        )
