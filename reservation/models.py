from datetime import date
from django.db import models
from django.utils import timezone
# Create your models here.

class Table(models.Model):
    number_of_seats = models.IntegerField()

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    group_size = models.IntegerField()
    date = models.DateField(default=timezone.localdate(timezone.now()), blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()


#timezone.now().strftime("%I:%M %p")