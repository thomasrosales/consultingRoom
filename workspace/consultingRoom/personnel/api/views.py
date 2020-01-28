from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from api.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from ..enums.months import Months
from calendar import monthrange
import datetime

from personnel.api.serializers import (
    PersonSerializer,
    PatientSerializer,
    DoctorSerializer,
    DocumentTypeSerializer,
    GenderTypeSerializer,
    CivilTypeSerializer,
    ScheduleSerializer,
    ScheduleStateSerializer,
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


class ScheduleStateList(generics.ListAPIView):
    queryset = ScheduleState.objects.all().filter(deleted=False)
    serializer_class = ScheduleStateSerializer


class ScheduleStateCreate(generics.CreateAPIView):
    queryset = ScheduleState.objects.all().filter(deleted=False)
    serializer_class = ScheduleStateSerializer


class ScheduleStateDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = ScheduleState
    queryset = ScheduleState.objects.all().filter(deleted=False)
    serializer_class = ScheduleStateSerializer


class DocumentList(generics.ListAPIView):
    queryset = DocumentType.objects.all().filter(deleted=False)
    serializer_class = DocumentTypeSerializer


class DocumentCreate(generics.CreateAPIView):
    queryset = DocumentType.objects.all().filter(deleted=False)
    serializer_class = DocumentTypeSerializer


class DocumentDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = DocumentType
    queryset = DocumentType.objects.all().filter(deleted=False)
    serializer_class = DocumentTypeSerializer


class GenderList(generics.ListAPIView):
    queryset = GenderType.objects.all().filter(deleted=False)
    serializer_class = GenderTypeSerializer


class GenderCreate(generics.CreateAPIView):
    queryset = GenderType.objects.all().filter(deleted=False)
    serializer_class = GenderTypeSerializer


class GenderDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = GenderType
    queryset = GenderType.objects.all().filter(deleted=False)
    serializer_class = GenderTypeSerializer


class CivilList(generics.ListAPIView):
    queryset = CivilType.objects.all().filter(deleted=False)
    serializer_class = CivilTypeSerializer


class CivilCreate(generics.CreateAPIView):
    queryset = CivilType.objects.all().filter(deleted=False)
    serializer_class = CivilTypeSerializer


class CivilDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = CivilType
    queryset = CivilType.objects.all().filter(deleted=False)
    serializer_class = CivilTypeSerializer


class PersonList(generics.ListAPIView):
    queryset = Person.objects.all().filter(deleted=False)
    serializer_class = PersonSerializer


class PersonCreate(generics.CreateAPIView):
    model = Person
    queryset = Person.objects.all().filter(deleted=False)
    serializer_class = PersonSerializer


class PersonDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = Person
    queryset = Person.objects.all().filter(deleted=False)
    serializer_class = PersonSerializer


class DoctorCreate(generics.CreateAPIView):
    queryset = Doctor.objects.all().filter(deleted=False)
    serializer_class = DoctorSerializer


class DoctorList(APIView, GenericListResponseLinked):
    model = Doctor

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'person': instance.person.to_json(),
            'deleted': instance.deleted
        }
        return instanceJson


class DoctorDetail(GenericResponseLinked, generics.RetrieveAPIView):
    model = Doctor
    serializer_class = DoctorSerializer

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'person': instance.person.to_json(),
            'deleted': instance.deleted
        }
        return instanceJson


class PatientList(APIView, GenericListResponseLinked):
    model = Patient

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'person': instance.person.to_json(),
            'born': instance.born,
            'year': instance.year,
            'checkIn': instance.checkIn,
            'document': instance.documentType.to_json(),
            'gender': instance.genderType.to_json(),
            'civil': instance.civilType.to_json(),
            'deleted': instance.deleted
        }
        return instanceJson


class PatientCreate(generics.CreateAPIView):
    queryset = Patient.objects.all().filter(deleted=False)
    serializer_class = PatientSerializer


class ScheduleList(APIView, GenericListResponseLinked):
    model = Schedule

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.id,
            'doctor': instance.doctor.to_json(),
            'startdate': instance.start_date.strftime("%m-%d-%Y %H:%M%p"),
            'enddate': instance.end_date.strftime("%m-%d-%Y %H:%M%p"),
            'status': instance.status.name,
            'deleted': instance.deleted
        }
        return instanceJson


class ScheduleCreate(generics.CreateAPIView):
    model = Schedule
    queryset = Schedule.objects.all().filter(deleted=False)
    serializer_class = ScheduleSerializer


class ScheduleDetail(
        generics.UpdateAPIView,
        GenericDeleteModel,
        generics.DestroyAPIView,
        generics.RetrieveAPIView):
    model = Schedule
    queryset = Schedule.objects.all().filter(deleted=False)
    serializer_class = ScheduleSerializer


class ScheduleByMoth(APIView):
    """Retorna para el mes recibido por parametro
    la cantidad de dias y los scheduler por dia

    Arguments:
        APIView {[type]} -- [description]
    """

    def get(self, request, year, month, format=None):
        if not month.upper() in Months._member_names_:
            return Response({'error': 'Month not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        schedules = Schedule.objects.all().filter(
            start_date__month=Months[month.upper()].value, start_date__year=year, deleted=False)
        result_set = {
            1: [1],
            2: [2],
            3: [3],
            4: [4],
            5: [5],
            6: [6],
            7: [7],
            8: [8],
            9: [9],
            10: [10],
            11: [11],
            12: [12],
            13: [13],
            14: [14],
            15: [15],
            16: [16],
            17: [17],
            18: [18],
            19: [19],
            20: [20],
            21: [21],
            22: [22],
            23: [23],
            24: [24],
            25: [25],
            26: [26],
            27: [27],
            28: [28],
            29: [29],
            30: [30],
            31: [31],
        }
        for sched in schedules:
            day = sched.start_date.day
            result_set[day].append(
                self.convert_to_json(sched))
        temp_result_set = []
        for temp in result_set:
            if not temp < int(datetime.datetime.now().day) and datetime.datetime.now().month == Months[month.upper()].value:
                temp_result_set.append(result_set[temp])
        return Response(temp_result_set)

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.pk,
            'doctor': instance.doctor.to_json(),
            'start_date': instance.start_date,
            'end_date': instance.end_date,
            'status': instance.status.to_json(),
            'deleted': instance.deleted
        }
        return instanceJson


class ScheduleByDate(APIView):

    def get(self, request, year, month, day, format=None):
        if not month.upper() in Months._member_names_:
            return Response({'error': 'Month not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        schedules = Schedule.objects.all().filter(
            start_date__month=Months[month.upper()].value,
            start_date__year=year,
            start_date__day=day,
            deleted=False)
        result_set = []
        for sched in schedules:
            day = sched.start_date.day
            result_set.append(self.convert_to_json(sched))
        return Response(result_set)

    def convert_to_json(self, instance):
        instanceJson = {
            'id': instance.pk,
            'doctor': instance.doctor.to_json(),
            'start_date': instance.start_date,
            'end_date': instance.end_date,
            'status': instance.status.to_json(),
            'deleted': instance.deleted
        }
        return instanceJson
