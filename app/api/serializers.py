
from rest_framework import serializers
from ..models import *


class ItemSerializer(serializers.ModelSerializer):

    country = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    lang = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = '__all__'
