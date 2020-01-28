from rest_framework import serializers
from datetime import datetime, date, time, timedelta
from rest_framework.validators import (
    UniqueValidator,
    UniqueForDateValidator,
    UniqueTogetherValidator
)

from treatment.models import (
    Appointment,
    TreatmentState,
    Treatment,
    Appointment,
    TreatmentHistory
)
from common.validations import instance_is_deleted


class TreatmentStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TreatmentState
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = '__all__'


class TreatmentHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TreatmentHistory
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    def validate_patient(self, value):
        instance_is_deleted(value, "person")
        return value

    def validate_treatment(self, value):
        instance_is_deleted(value, "name")
        return value

    class Meta:
        model = Appointment
        fields = '__all__'
