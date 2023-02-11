from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mer_pk):
    measurement = Measurement.objects.get(pk=mer_pk)
    return measurement

def create_measurement(mer):
    measurement = Measurement(unit = mer["unit"], value = mer["value"], place = mer["place"], dateTime = mer["dateTime"], variable = mer["variable"])
    measurement.save()
    return measurement

def update_measurement(mer_pk, mer):
    measurement = get_measurement(mer_pk)
    measurement.unit = mer["unit"]
    measurement.value = mer["value"]
    measurement.place = mer["place"]
    measurement.dateTime = mer["dateTime"]
    measurement.variable = mer["variable"]
    measurement.save()
    return measurement
