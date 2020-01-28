from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    brand = models.CharField(max_length=200)
    representation = models.CharField(max_length=200)
    stock = models.IntegerField()
    register = models.CharField(max_length=200)
    risk = models.CharField(max_length=200)
    photo = models.ImageField(
        upload_to='images/inventory/', blank=True, default='images/inventory/name.png')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_json(self):
        data = {}
        data['id'] = self.pk
        data['name'] = self.name
        data['brand'] = self.brand
        data['representation'] = self.representation
        data['stock'] = self.stock
        data['register'] = self.register
        data['risk'] = self.risk
        data['image'] = self.photo.name
        data['deleted'] = self.deleted
        return data
