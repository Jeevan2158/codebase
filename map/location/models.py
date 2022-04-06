from django.db import models

class locate(models.Model):
    long = models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3,blank=True, null=True)
