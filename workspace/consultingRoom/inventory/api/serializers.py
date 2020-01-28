from rest_framework import serializers
from datetime import datetime, date, time, timedelta
from rest_framework.validators import (
    UniqueValidator,
    UniqueForDateValidator,
    UniqueTogetherValidator
)

from inventory.models import (
    Inventory
)

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'