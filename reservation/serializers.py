from pyexpat import model
from rest_framework import serializers
from .models import Reservation

class CraeteReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["group_size","table", "date", "start_time", "end_time"]

class ListReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'