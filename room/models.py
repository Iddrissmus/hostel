from django.db import models

# Create your models here.
class Guest(models.Model):
    guest_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    room_id = models.IntegerField()
    date_arrived = models.DateField(auto_now=True)

class Room(models.Model):
    room_type = models.CharField(max_length=20)
    price = models.IntegerField()
    occupancy = models.IntegerField()
    availability = models.CharField(max_length=20)