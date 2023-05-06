from django.shortcuts import render
from .logic import historiaClinica_logic as l
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from widmy_Project.auth0backend import getRole

rolesValidos = ["Doctor", "Enfermero", "AdministradorSistema"]

@csrf_exempt
@login_required
def HistoriasClinicas_view(request):
	role = getRole(request)
	if role in rolesValidos:
		if request.method == 'GET':
			id = request.GET.get("id",None)
			if id:
				hc_dto = l.get_HistoriaClinica(id)
				hc = serializers.serialize('json',[hc_dto,])
				return HttpResponse(hc, 'application/json')
			else:
				hcs_dto = l.get_all_HistoriaClinica()
				hcs = serializers.serialize('json', hcs_dto)
				return HttpResponse(hcs, 'application/json')
		if request.method == 'POST':
			hc_dto = l.create_HistoriaClinica(json.loads(request.body))
			hc = serializers.serialize('json', [hc_dto, ])
			return HttpResponse(hc, 'application/json')
	else:
		return HttpResponse("Unauthorized User")

@csrf_exempt
@login_required
def HistoriaClinica_view(request, pk):
	role = getRole(request)
	if role in rolesValidos:
		if request.method == 'GET':
			hc_dto = l.get_HistoriaClinica(pk)
			hc = serializers.serialize('json', [hc_dto,])
			return HttpResponse(hc, 'application/json')
		if request.method == 'PUT':
			hc_dto = l.update_HistoriaClinica(pk, json.loads(request.body))
			hc = serializers.serialize('json', [hc_dto,])
			return HttpResponse(hc, 'application/json')
		if request.method == 'DELETE':
			hc_dto = l.delete_HistoriaClinica(pk)
			hc = serializers.serialize('json', [hc_dto,])
			return HttpResponse(hc, 'application/json')
	else:
		return HttpResponse("Unauthorized User")
