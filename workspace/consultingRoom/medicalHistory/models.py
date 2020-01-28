from django.db import models
from django.utils import timezone
from personnel.models import(
    Patient
)

# Create your models here.


class BasicInfo(models.Model):
    associate_with = models.CharField(max_length=200)
    associate_celphone = models.IntegerField()
    reason = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    antecedent = models.CharField(max_length=200)
    family_antecedent = models.CharField(max_length=200)
    surgical_antecedent = models.CharField(max_length=200)
    pathological_antecedent = models.CharField(max_length=200)
    pharm_antecedent = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['associate_with'] = self.associate_with
        data['associate_celphone'] = self.associate_celphone
        data['antecedent'] = self.antecedent
        data['reason'] = self.reason
        data['disease'] = self.disease
        data['family_antecedent'] = self.family_antecedent
        data['surgical_antecedent'] = self.surgical_antecedent
        data['pathological_antecedent'] = self.pathological_antecedent
        data['pharm_antecedent'] = self.pharm_antecedent
        data['deleted'] = self.deleted
        return data


class Consent(models.Model):
    conset_date = models.DateField(auto_now_add=True)
    usage_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    deleted = models.BooleanField(default=False)

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['conset_date'] = self.conset_date
        data['usage_date'] = self.usage_date
        data['description'] = self.description
        data['deleted'] = self.deleted
        return data


class MedicalHistory(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.DO_NOTHING)
    basic_info = models.OneToOneField(BasicInfo, on_delete=models.DO_NOTHING)
    consent = models.OneToOneField(Consent, on_delete=models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.person.idDocument + " / " + self.date.strftime("%m-%d-%Y %H:%M%p")

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['patient'] = self.patient.to_json()
        data['basic_info'] = self.basic_info.to_json()
        data['consent'] = self.consent.to_json()
        data['date'] = self.date
        data['time'] = self.time
        data['deleted'] = self.deleted
        return data
