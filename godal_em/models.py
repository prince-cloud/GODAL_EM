from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Region(models.Model):
    name = models.CharField(max_length=100)
    
class Meter(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="meter")
    meter_id = models.CharField(max_length=8, unique=True)
    current_power = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.meter_id

class Request(models.Model):
    by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    granted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        # if unique_id
        #self.invoice_id = str(self.supplier.id + unique_id(8))
        self.by.meter.current_power += self.amount
        self.by.meter.save()
        super().save(*args, **kwargs)

