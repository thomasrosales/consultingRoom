from django.urls import path
from personnel.api import views as person_views
from treatment.api import views as treatment_views
from medicalHistory.api import views as medical_views
from inventory.api import views as inventory_views
from account.api import views as user_views

from . import views

app_name = 'api'

urlpatterns = [
    path('get_token/', views.CustomAuthToken.as_view())
]

urlpatterns += [
    path('personnel/person/list', person_views.PersonList.as_view()),
    path('personnel/person/create', person_views.PersonCreate.as_view()),
    path('personnel/person/<int:pk>/detail',
         person_views.PersonDetail.as_view()),
    path('personnel/patient/list', person_views.PatientList.as_view()),
    path('personnel/patient/create', person_views.PatientCreate.as_view()),
    path('personnel/doctor/list', person_views.DoctorList.as_view()),
    path('personnel/doctor/create', person_views.DoctorCreate.as_view()),
    path('personnel/doctor/<int:pk>/detail',
         person_views.DoctorDetail.as_view()),
    path('personnel/schedule/list',
         person_views.ScheduleList.as_view()),
    path('personnel/schedule/create', person_views.ScheduleCreate.as_view()),
    path('personnel/schedule/<int:pk>/detail',
         person_views.ScheduleDetail.as_view()),
    path('personnel/schedule/state/list',
         person_views.ScheduleStateList.as_view()),
    path('personnel/schedule/state/create',
         person_views.ScheduleStateCreate.as_view()),
    path('personnel/schedule/state/<int:pk>/detail',
         person_views.ScheduleStateDetail.as_view()),
    path('personnel/document/list',
         person_views.DocumentList.as_view()),
    path('personnel/document/create', person_views.DocumentCreate.as_view()),
    path('personnel/document/<int:pk>/detail',
         person_views.DocumentDetail.as_view()),
    path('personnel/gender/list', person_views.GenderList.as_view()),
    path('personnel/gender/create', person_views.GenderCreate.as_view()),
    path('personnel/gender/<int:pk>/detail',
         person_views.GenderDetail.as_view()),
    path('personnel/civil/list', person_views.CivilList.as_view()),
    path('personnel/civil/create', person_views.CivilCreate.as_view()),
    path('personnel/civil/<int:pk>/detail',
         person_views.CivilDetail.as_view()),
]

urlpatterns += [
    path('treatment/treatment/state/list',
         treatment_views.TreatmentStateList.as_view()),
    path('treatment/treatment/state/create',
         treatment_views.TreatmentStateCreate.as_view()),
    path('treatment/treatment/state/<int:pk>/detail',
         treatment_views.TreatmentStateDetail.as_view()),
    path('treatment/treatment/list',
         treatment_views.TreatmentList.as_view()),
    path('treatment/treatment/create',
         treatment_views.TreatmentCreate.as_view()),
    path('treatment/treatment/<int:pk>/detail',
         treatment_views.TreatmentDetail.as_view()),
    path('treatment/historical/treatment/list',
         treatment_views.TreatmentHistoryList.as_view()),
    path('treatment/historical/treatment/create',
         treatment_views.TreatmentHistoryCreate.as_view()),
    path('treatment/historical/treatment/<int:pk>/detail',
         treatment_views.TreatmentHistoryDetail.as_view()),
    path('treatment/appointment/list',
         treatment_views.AppointmentList.as_view()),
    path('treatment/appointment/create',
         treatment_views.AppointmentCreate.as_view()),
]

urlpatterns += [
    path('medical/basic/info/create', medical_views.BasicInfoCreate.as_view()),
    path('medical/basic/info/<int:pk>/detail',
         medical_views.BasicInfoDetail.as_view()),
    path('medical/consent/create', medical_views.ConsentCreate.as_view()),
    path('medical/consent/<int:pk>/detail',
         medical_views.ConsentDetail.as_view()),
    path('medical/history/list', medical_views.MedicalHistoryList.as_view()),
    path('medical/history/create', medical_views.MedicalHistoryCreate.as_view()),
    path('medical/history/<int:pk>/detail',
         medical_views.MedicalHistoryDetail.as_view()),
    path('medical/history/<int:pk>/update',
         medical_views.MedicalHistoryUpdate.as_view()),
]

urlpatterns += [
    path('inventory/list',
         inventory_views.InventoryList.as_view()),
    path('inventory/create', inventory_views.InventoryCreate.as_view()),
    path('inventory/<int:pk>/detail', inventory_views.InventoryDetail.as_view()),
]

urlpatterns += [
    path('account/user/<int:pk>/detail', user_views.UserDetail.as_view()),
    path('account/user/create', user_views.UserCreate.as_view()),
]

urlpatterns += [
    path('schedulers/<int:year>/<slug:month>',
         person_views.ScheduleByMoth.as_view()),
    path('schedulers/<int:year>/<slug:month>/<int:day>',
         person_views.ScheduleByDate.as_view()),
]
