from django.db import models
from personnel.models import(
    Doctor,
    Patient,
    Schedule
)

# Create your models here.


class TreatmentState(models.Model):
    name = models.CharField(max_length=200, unique=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['name'] = self.name
        data['deleted'] = self.deleted
        return data


class Treatment(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['name'] = self.name
        data['description'] = self.description
        data['price'] = self.price
        data['deleted'] = self.deleted
        return data


class Appointment(models.Model):
    schedule = models.OneToOneField(Schedule, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    treatment = models.ForeignKey(Treatment, on_delete=models.DO_NOTHING)
    assistance = models.CharField(max_length=200)
    description = models.TextField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.person.idDocument + ' - ' + self.treatment.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['schedule'] = self.schedule.to_json()
        data['patient'] = self.patient.to_json()
        data['treatment'] = self.treatment.to_json()
        data['description'] = self.description
        data['assistance'] = self.assistance
        data['deleted'] = self.deleted
        return data


class TreatmentHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    treatment = models.ForeignKey(Treatment, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(TreatmentState, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.person.idDocument + ' - ' + self.status.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['patient'] = self.patient.to_json()
        data['treatment'] = self.treatment.to_json()
        data['status'] = self.status.to_json()
        data['price'] = self.price
        data['deleted'] = self.deleted
        return data
