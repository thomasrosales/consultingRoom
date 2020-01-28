from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from api.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins


from treatment.api.serializers import (
    TreatmentStateSerializer,
    TreatmentSerializer,
    TreatmentHistorySerializer,
    AppointmentSerializer
)
from treatment.models import (
    Appointment,
    TreatmentState,
    Treatment,
    Appointment,
    TreatmentHistory
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
from common.views import GenericDeleteModel, GenericListResponseLinked, GenericResponseLinked


class TreatmentStateList(generics.ListAPIView):
    queryset = TreatmentState.objects.all().filter(deleted=False)
    serializer_class = TreatmentStateSerializer


class TreatmentStateCreate(generics.CreateAPIView):
    queryset = TreatmentState.objects.all().filter(deleted=False)
    serializer_class = TreatmentStateSerializer


class TreatmentStateDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = TreatmentState
    queryset = TreatmentState.objects.all().filter(deleted=False)
    serializer_class = TreatmentStateSerializer


class TreatmentList(generics.ListAPIView):
    queryset = Treatment.objects.all().filter(deleted=False)
    serializer_class = TreatmentSerializer


class TreatmentCreate(generics.CreateAPIView):
    queryset = Treatment.objects.all().filter(deleted=False)
    serializer_class = TreatmentSerializer


class TreatmentDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = Treatment
    queryset = Treatment.objects.all().filter(deleted=False)
    serializer_class = TreatmentSerializer


class TreatmentHistoryList(APIView, GenericListResponseLinked):
    model = TreatmentHistory

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'patient': instance.patient.to_json(),
            'treatment': instance.treatment.to_json(),
            'status': instance.status.to_json(),
            'price': instance.price,
            'deleted': instance.deleted
        }
        return instanceJson


class TreatmentHistoryCreate(generics.CreateAPIView):
    queryset = TreatmentHistory.objects.all().filter(deleted=False)
    serializer_class = TreatmentHistorySerializer


class TreatmentHistoryDetail(GenericResponseLinked, generics.RetrieveAPIView):
    model = TreatmentHistory
    serializer_class = TreatmentHistorySerializer

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'patient': instance.patient.to_json(),
            'treatment': instance.treatment.to_json(),
            'status': instance.status.to_json(),
            'price': instance.price,
            'deleted': instance.deleted
        }
        return instanceJson


class AppointmentList(APIView, GenericListResponseLinked):
    model = Appointment

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'schedule': instance.schedule.to_json(),
            'patient': instance.patient.to_json(),
            'treatment': instance.treatment.to_json(),
            'description': instance.description,
            'assistance': instance.assistance,
            'deleted': instance.deleted
        }
        return instanceJson


class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all().filter(deleted=False)
    serializer_class = AppointmentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            treatment = Treatment.objects.get(pk=serializer.data['treatment'])
            treatmentHistoryData = {
                'patient': serializer.data['patient'],
                'treatment': treatment.pk,
                'status': TreatmentState.objects.get(name='COMPLETED').pk,
                'price': treatment.price
            }
            historicalSerializer = TreatmentHistorySerializer(
                data=treatmentHistoryData)
            if historicalSerializer.is_valid():
                historicalSerializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
