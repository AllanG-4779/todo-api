from rest_framework import serializers
from .models import Item
"""
 A serializer is used to convert the data from the model in a way that can be used in the web 
 in json format or xml format etc.
"""

class ItemSerializer(serializers.ModelSerializer):
    class Meta:

        model = Item
        fields = "__all__"
