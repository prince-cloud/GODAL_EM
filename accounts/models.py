from django.contrib.auth.models import AbstractUser
from django.db import models
#from godal_em.models import Region

class CustomUser(AbstractUser):
    house_number = models.CharField(max_length=100)
    #region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    digital_address = models.CharField(max_length=20)
    house_type = models.CharField(max_length=100)

    def __str__(self):
        return self.email