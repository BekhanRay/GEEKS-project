
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ItemSerializer
from ..models import Item


class ItemList(APIView):
    # @api_view(['GET'])
    def get(self, request):

        # if request.method == 'GET':
        data = Item.objects.all()
        serializer = ItemSerializer(data, many=True)
        return Response(serializer.data)


# class FilteredList(APIView):
#     def post(self, request):
#         # Getting data from the POST request
#         builder = request.data.get('builder')
#         apartment_square = request.data.get('apartment_square')
#         room_id = request.data.get('room_id')  # assuming it comes with the room ID
#         type_id = request.data.get('type_id')  # assuming it comes with the type ID
#         country_id = request.data.get('country_id')  # country ID
#         city_id = request.data.get('city_id')  # city ID
#         district_id = request.data.get('district_id')  # district ID
#         lang_id = request.data.get('lang_id')  # language ID
#
#         # Filtering Item objects
#         filtered_items = Item.objects.filter(
#             builder=builder,
#             apartment_square=apartment_square,
#             room_id=room_id,
#             type_id=type_id,
#             country_id=country_id,
#             city_id=city_id,
#             district_id=district_id,
#             lang_id=lang_id
#         )
#
#         # Serializing the filtered data
#         serializer = ItemSerializer(filtered_items, many=True)
#
#         return Response(serializer.data)


class FilteredList(APIView):
    def get(self, request):

        filtered_items = Item.objects.all()

        # Serialize the filtered data
        serialized_data = ItemSerializer(filtered_items, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)

        # # Creating custom response format
        # custom_response = [
        #     {
        #         "id": item['id'],
        #         "country": item['country']['name'],
        #         "city": item['city']['name'],
        #         "district": item['district']['name'],
        #         "type": item['type']['name'],
        #         "lang": item['lang']['name'],
        #         "photos": item['photos'].url if item['photos'] else None,
        #         "name": item['name'],
        #         "description": item['description'],
        #         "builder": item['builder'],
        #         "apartment_square": item['apartment_square'],
        #         "file": item['file'].url if item['file'] else None,
        #         "room": item['room']
        #     }
        #     for item in serialized_data
        # ]
        #
        # return Response(custom_response, status=status.HTTP_200_OK)

