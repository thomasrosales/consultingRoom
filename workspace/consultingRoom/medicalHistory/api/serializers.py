from rest_framework import serializers
from datetime import datetime, date, time, timedelta
from rest_framework.validators import (
    UniqueValidator,
    UniqueForDateValidator,
    UniqueTogetherValidator
)

from medicalHistory.models import (
    BasicInfo,
    Consent,
    MedicalHistory,
)
from common.validations import instance_is_deleted


class ConsentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consent
        fields = '__all__'


class BasicInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasicInfo
        fields = '__all__'


class MedicalHistorySerializer(serializers.ModelSerializer):

    def validate_patient(self, value):
        instance_is_deleted(value, "person")
        return value

    def validate_basic_info(self, value):
        instance_is_deleted(value, "associate_with")
        return value

    def validate_consent(self, value):
        instance_is_deleted(value, "conset_date")
        return value

    class Meta:
        model = MedicalHistory
        fields = '__all__'
