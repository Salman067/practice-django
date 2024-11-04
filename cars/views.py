from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_list_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CarsViewset(APIView):
    def get(self, request,id=None):
        if id:
            car = models.Cars.objects.get(id=id)
            serializer = serializers.CarSerializer(car)
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            cars = models.Cars.objects.all()
            serializer = serializers.CarSerializer(cars, many=True)
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        
    def post(self, request):
        serializer = serializers.CarSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'Car created successfully'}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({'status':'error', 'message':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id=None):
        car = models.Cars.objects.get(id=id)
        serializer = serializers.CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'Car updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'message':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id=None):
        car = models.Cars.objects.filter(id=id)
        car.delete()
        return Response({'status':'success', 'message':'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)