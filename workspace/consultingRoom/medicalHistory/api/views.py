from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from api.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from medicalHistory.api.serializers import (
    ConsentSerializer,
    BasicInfoSerializer,
    MedicalHistorySerializer,
)
from medicalHistory.models import (
    BasicInfo,
    Consent,
    MedicalHistory,
)
from personnel.models import (
    Patient,
)
from common.views import GenericDeleteModel, GenericListResponseLinked, GenericResponseLinked


class BasicInfoCreate(generics.CreateAPIView):
    queryset = BasicInfo.objects.all().filter(deleted=False)
    serializer_class = BasicInfoSerializer


class BasicInfoDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = BasicInfo
    queryset = BasicInfo.objects.all().filter(deleted=False)
    serializer_class = BasicInfoSerializer


class ConsentCreate(generics.CreateAPIView):
    queryset = Consent.objects.all().filter(deleted=False)
    serializer_class = ConsentSerializer


class ConsentDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = Consent
    queryset = Consent.objects.all().filter(deleted=False)
    serializer_class = ConsentSerializer


class MedicalHistoryList(APIView, GenericListResponseLinked):
    model = MedicalHistory

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'patient': instance.patient.to_json(),
            'basic_info': instance.basic_info.to_json(),
            'consent': instance.consent.to_json(),
            'date': instance.date,
            'time': instance.time,
            'deleted': instance.deleted
        }
        return instanceJson


class MedicalHistoryCreate(generics.CreateAPIView):
    queryset = MedicalHistory.objects.all().filter(deleted=False)
    serializer_class = MedicalHistorySerializer


class MedicalHistoryDetail(
        GenericResponseLinked,
        generics.RetrieveAPIView):
    model = MedicalHistory
    queryset = MedicalHistory.objects.all().filter(deleted=False)
    serializer_class = MedicalHistorySerializer

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'patient': instance.patient.to_json(),
            'basic_info': instance.basic_info.to_json(),
            'consent': instance.consent.to_json(),
            'date': instance.date,
            'time': instance.time,
            'deleted': instance.deleted
        }
        return instanceJson


class MedicalHistoryUpdate(generics.UpdateAPIView):
    queryset = MedicalHistory.objects.all().filter(deleted=False)
    serializer_class = MedicalHistorySerializer
