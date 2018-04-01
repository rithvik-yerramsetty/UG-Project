from django.db import models


# Create your models here.

class Substation(models.Model):
    substation_name = models.CharField(max_length=250)
    HT_CurrentValue = models.FloatField()
    HT_VoltageValue = models.FloatField()
    HT_PowerFactor = models.FloatField()
    LT_CurrentValue = models.FloatField()
    LT_VoltageValue = models.FloatField()
    LT_PowerFactor = models.FloatField()

    def __str__(self):
        return self.substation_name

