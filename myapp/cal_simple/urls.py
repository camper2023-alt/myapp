from django.urls import path
from . import views

app_name = 'cal_simple'

urlpatterns = [
    path('', views.cal, name='cal'),
    path('result', views.result, name='result')
]