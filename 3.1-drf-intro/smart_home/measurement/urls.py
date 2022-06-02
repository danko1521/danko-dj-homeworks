from django.urls import path
from .views import TemperatureView, SensorsView

urlpatterns = [
    path('temperature/', TemperatureView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
