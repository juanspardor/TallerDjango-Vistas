from ..models import Measurement
from ..models import Variable
from django.db import models


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mer_pk):
    measurement = Measurement.objects.get(pk=mer_pk)
    return measurement

def create_measurement(mer):
    pVariable = Variable.objects.get(pk=mer["variable"])
    measurement = Measurement(unit = mer["unit"], value = mer["value"], place = mer["place"], dateTime = mer["dateTime"], variable = pVariable)
    measurement.save()
    return measurement

def update_measurement(mer_pk, mer):
    pVariable = Variable.objects.get(pk=mer["variable"])
    measurement = get_measurement(mer_pk)
    measurement.unit = mer["unit"]
    measurement.value = mer["value"]
    measurement.place = mer["place"]
    measurement.dateTime = mer["dateTime"]
    measurement.variable = pVariable
    measurement.save()
    return measurement

def delete_measurement(mer_pk):
    measurement = Measurement.objects.get(pk = mer_pk).delete()
    return measurement