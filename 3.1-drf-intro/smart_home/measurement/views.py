# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer


class TemperatureView(APIView):
    def get(self, request):
        temperatures = Measurement.objects.all()
        temper = MeasurementSerializer(temperatures, many=True)
        return Response(temper.data)

    def post(self, request):
        temp = MeasurementSerializer(data=request.data)
        if temp.is_valid():
            if request.data.get('id'):
                ids = request.data.get(id)
                temp.save(id=ids)
            else:
                temp.save()
        return Response({'status': 'OK'})


class SensorsView(APIView):
    def get(self, request):
        temp_sensors = SensorSerializer.objects.all()
        sens = SensorSerializer(temp_sensors, many=True)
        return Response(sens.data)

    def post(self, request):
        sens = SensorSerializer(data=request.data)
        if sens.is_valid():
            if request.data.get('id'):
                ids = request.data.get(id)
                sens.save(id=ids)
            else:
                sens.save()
        return Response({'status': 'OK'})
