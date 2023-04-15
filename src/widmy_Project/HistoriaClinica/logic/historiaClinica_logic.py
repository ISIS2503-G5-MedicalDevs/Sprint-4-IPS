import datetime

from ..models import HistoriaClinica
from django.db import models

def get_all_HistoriaClinica():
	historiaclinica = HistoriaClinica.objects.using('HistoriaClinica').all()
	return HistoriaClinica

def get_HistoriaClinica(historia_pk):
	historiaclinica = HistoriaClinica.objects.using('HistoriaClinica').get(pk=historia_pk)
	return HistoriaClinica

def create_HistoriaClinica(hc):
	historiaclinica = HistoriaClinica(
		motivoConsulta = hc['motivoConsulta'],
		enfermedadActual = hc['enfermedadActual'],
		analisis = hc['analisis'],
		diagnostico = hc['diagnostico'],
		procedimiento = hc['procedimiento'],
		fecha = datetime.date.today(),
		hora = datetime.datetime.now().time()
	)
	historiaclinica.save(using='HistoriaClinica')
	return historiaclinica

def update_HistoriaClinica(hc_pk, hc):
	historiaclinica = get_HistoriaClinica(hc_pk)
	historiaclinica.motivoConsulta = hc['motivoConsulta']
	historiaclinica.enfermedadActual = hc['enfermedadActual']
	historiaclinica.analisis = hc['analisis']
	historiaclinica.diagnostico = hc['diagnostico']
	historiaclinica.procedimiento = hc['procedimiento']
	historiaclinica.fecha = datetime.datetime.strptime(hc['fecha'], '%m/%d/%Y').date()
	historiaclinica.hora = datetime.datetime.strptime(hc['fecha'], '%H:%M:%S.%f').time()
	historiaclinica.save(using='HistoriaClinica')
	return historiaclinica

def delete_HistoriaClinica(hc_pk):
	historiaclinica = get_HistoriaClinica(hc_pk)
	historiaclinica.delete()
	return historiaclinica