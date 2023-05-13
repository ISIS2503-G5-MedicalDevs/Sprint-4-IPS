from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path('', views.HistoriasClinicas_view, name='HistoriasClinicas_view'),
	path('<int:pk>', views.HistoriaClinica_view, name = 'HistoriaClinica_view'),
    path('test', views.HistoriaClinica_test, name = 'HistoriaClinica_test')
]