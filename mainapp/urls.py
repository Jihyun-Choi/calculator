from django.urls import path
from mainapp.views import CalculatorView

app_name = 'mainapp'

urlpatterns = [
    path('calculator/', CalculatorView.as_view(), name='calculator'),
]
