from rest_framework import serializers
from .models import *

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')



# class LocationSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('__all__')