from rest_framework.views import APIView
from rest_framework.response import Response

class ListView(APIView):
    def get(self, request):
        return Response(
            {
                "leaflet a": "/a",
                "leaflet b": "/b",
            }
        )
