from rest_framework import serializers
from . import models

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cars
        fields = ('id', 'car_name', 'car_version', 'car_model')
        # fields='__all__'