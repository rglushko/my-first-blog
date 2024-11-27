
from django.db import models

class Certificate(models.Model):
    serial_number = models.CharField(max_length=100)
    article_number = models.CharField(max_length=100)
    date_end = models.DateField()
    name_pump = models.CharField(max_length=100)
    wc_number = models.CharField(max_length=100)
    name_partner = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)