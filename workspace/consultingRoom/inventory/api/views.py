from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from api.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from inventory.models import (
    Inventory
)
from inventory.api.serializers import (
    InventorySerializer
)
from common.views import GenericDeleteModel, GenericListResponseLinked, GenericResponseLinked


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all().filter(deleted=False)
    serializer_class = InventorySerializer


class InventoryCreate(generics.CreateAPIView):
    queryset = Inventory.objects.all().filter(deleted=False)
    serializer_class = InventorySerializer


class InventoryDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = Inventory
    queryset = Inventory.objects.all().filter(deleted=False)
    serializer_class = InventorySerializer
