from django.shortcuts import render, redirect
from rest_framework import generics
from .models import *
from .serializers import *


def sorry(request):
    return render(request, "sorry.html")


class PostList(generics.ListCreateAPIView):
    serializer_class = TaskSerializers


    def get_queryset(self):
        queryset = Task.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(taskLocation=location)
        return queryset
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()



# class LocationList(generics.ListCreateAPIView):
#     serializer_class = LocationSerializers
#     queryset = Location.objects.all()




# class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = LocationSerializers
#     queryset = Location.objects.all()
