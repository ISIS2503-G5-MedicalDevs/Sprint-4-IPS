from django.db import models


class HistoriaClinica(models.Model):
	motivoConsulta = models.CharField(max_length = 200)
	enfermedadActual = models.CharField(max_length = 50)
	analisis = models.CharField(max_length = 200)
	diagnostico = models.CharField(max_length = 200)
	procedimiento = models.CharField(max_length = 200)
	fecha = models.DateField()
	hora = models.TimeField()

	def __str__(self) ->str:
		return '%s, %s, %s' (self.pk, self.fecha, self.hora)

