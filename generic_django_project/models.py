__author__ = 'pridemai'

from django.db import models

class Cars(models.Model):
    year = models.IntegerField(default=0)
    make = models.CharField(default="N/A", max_length=150)
    model = models.CharField(default="N/A", max_length=150)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        pass