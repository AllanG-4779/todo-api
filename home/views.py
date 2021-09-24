

from .models import Item
from .Serializers import ItemSerializer
from rest_framework import viewsets

# Create your views here.
"""
 These class based views are used to create api views
"""
# class ItemsView(generics.ListAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class CreateItemView(generics.CreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

class ItemManipulationViews(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    