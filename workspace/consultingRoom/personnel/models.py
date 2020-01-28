from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    idDocument = models.CharField(max_length=200, unique=True)
    celphone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.lastname

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['name'] = self.name
        data['lastname'] = self.lastname
        data['idDocument'] = self.idDocument
        data['celphone'] = self.celphone
        data['email'] = self.email
        data['address'] = self.address
        data['deleted'] = self.deleted
        return data


class ScheduleState(models.Model):
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


class Doctor(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, unique=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.person.name + ' ' + self.person.lastname + ' - Document: ' + self.person.idDocument

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['person'] = self.person.to_json()
        data['deleted'] = self.deleted
        return data


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.ForeignKey(ScheduleState, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.start_date.strftime("%m-%d-%Y %H:%M%p") + ' - ' + self.end_date.strftime("%m-%d-%Y %H:%M%p") + ' - ' + self.status.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['doctor'] = self.doctor.to_json()
        data['startdate'] = self.start_date
        data['enddate'] = self.end_date
        data['status'] = self.status.to_json()
        data['deleted'] = self.deleted
        return data


class DocumentType(models.Model):
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


class GenderType(models.Model):
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


class CivilType(models.Model):
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


class Patient(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, unique=True)
    born = models.DateField()
    year = models.IntegerField()
    checkIn = models.DateField()
    documentType = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING)
    genderType = models.ForeignKey(GenderType,  on_delete=models.DO_NOTHING)
    civilType = models.ForeignKey(CivilType, on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.person.name + ' ' + self.person.lastname + ' - Document: ' + self.person.idDocument

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['person'] = self.person.to_json()
        data['born'] = self.born
        data['year'] = self.year
        data['checkIn'] = self.checkIn
        data['document'] = self.documentType.to_json()
        data['gender'] = self.genderType.to_json()
        data['civil'] = self.civilType.to_json()
        data['deleted'] = self.deleted
        return data
