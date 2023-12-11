
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ItemSerializer
from ..models import Item


class ItemList(APIView):
    # @api_view(['GET'])
    def get(self, request):

        # if request.method == 'GET':
        data = Item.objects.all()
        serializer = ItemSerializer(data, many=True)
        return Response(serializer.data)


