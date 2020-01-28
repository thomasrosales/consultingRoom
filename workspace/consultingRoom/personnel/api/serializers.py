from rest_framework import serializers
from datetime import datetime, date, time, timedelta
from rest_framework.validators import (
    UniqueValidator,
    UniqueForDateValidator,
    UniqueTogetherValidator
)

from personnel.models import (
    Person,
    Doctor,
    Patient,
    Schedule,
    ScheduleState,
    DocumentType,
    GenderType,
    CivilType
)
from common.validations import instance_is_deleted


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):

    def validate_person(self, value):
        instance_is_deleted(value, "idDocument")
        return value

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    def validate_person(self, value):
        instance_is_deleted(value, "idDocument")
        return value

    def validate_documentType(self, value):
        instance_is_deleted(value, "name")
        return value

    def validate_genderType(self, value):
        instance_is_deleted(value, "name")
        return value

    def validate_civilType(self, value):
        instance_is_deleted(value, "name")
        return value

    class Meta:
        model = Patient
        fields = '__all__'


class ScheduleStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleState
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):

    def validate_doctor(self, value):
        instance_is_deleted(value, "person")
        return value

    def validate_status(self, value):
        instance_is_deleted(value, "name")
        return value

    def validate(self, data):
        past_day_error = "It's not possible load past dates."
        date_error = "The end time {} is shorter than start time {}."
        scheduler_error = "To the range {} to {} exists another scheduler."
        schedulers = Schedule.objects.all().filter(start_date__gte=date.today(),
                                                   doctor=data['doctor']).order_by('-pk')
        if schedulers != None and len(schedulers) != 0:
            if data['end_date'].time() < data['start_date'].time():
                raise serializers.ValidationError(
                    date_error.format(data['end_date'], data['start_date']))
            elif data['end_date'] < date.today() or data['start_date'] < date.today():
                raise serializers.ValidationError(past_day_error)
            for schedule in schedulers:
                if data['start_date'].time() >= schedule.start_date.time():
                    raise serializers.ValidationError(
                        scheduler_error.format(data['end_date'], data['start_date']))
                elif data['end_date'].time() > schedule.start_date.time():
                    raise serializers.ValidationError(
                        scheduler_error.format(data['end_date'], data['start_date']))
        return data

    class Meta:
        model = Schedule
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['doctor', 'start_date', 'end_date']
            )
        ]


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = '__all__'


class GenderTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenderType
        fields = '__all__'


class CivilTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CivilType
        fields = '__all__'
