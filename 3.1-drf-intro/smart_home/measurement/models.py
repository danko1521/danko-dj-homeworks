from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField()
    date_current = models.DateTimeField(auto_now=True)
    id_Sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
