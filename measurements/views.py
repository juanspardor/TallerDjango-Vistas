from django.shortcuts import render
from .logic import logic_measurements as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')
      
    if request.method =='POST':
        variable_dto = ml.create_measurement(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ml.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'DELETE':
        measurement_dto = ml.delete_measurement(pk)
        return HttpResponse(status = 200)
    
    if request.method == 'PUT':
        measurement_dto = ml.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')