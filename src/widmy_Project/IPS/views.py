from django.shortcuts import render
from .logic import IPS_logic as l
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from widmy_Project.auth0backend import getRole
import widmy_Project.validate as vl

rolesValidos = ["Administrador", "AdministradorSistema"]

@csrf_exempt
@login_required
def IPSs_view(request):
    
    if request.method == 'POST':
            IPS_dto = l.create_IPS(json.loads(request.body))
            ips = serializers.serialize('json', [IPS_dto, ])
            return HttpResponse(ips, 'application/json')
    
    role = getRole(request)
    if role in rolesValidos:
        if request.method=='GET':
            id = request.GET.get("id",None)
            if id:
                IPS_dto = l.get_IPS(id)
                ips = serializers.serialize('json',[IPS_dto,])
                return HttpResponse(ips, 'application/json')
            else:
                IPSs_dto = l.get_IPSs()
                IPSs = serializers.serialize('json', IPSs_dto)
                return HttpResponse(IPSs, 'application/json')
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
@login_required
def IPS_view(request, pk):
    role = getRole(request)
    if role in rolesValidos:
        if request.method == 'GET':
            IPS_dto = l.get_IPS(pk)
            ips = serializers.serialize('json', [IPS_dto,])
            return HttpResponse(ips, 'application/json')
        if request.method == 'PUT':
            if not(vl.validar(json.loads(request.body))):
                return HttpResponseBadRequest(HttpResponse("Error, invalid entry for update"))
            IPS_dto = l.update_IPS(pk, json.loads(request.body))
            ips = serializers.serialize('json', [IPS_dto,])
            return HttpResponse(ips, 'application/json')
        if request.method == 'DELETE':
            IPS_dto = l.delete_IPS(pk)
            ips = serializers.serialize('json', [IPS_dto,])
            return HttpResponse(ips, 'application/json')
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
def IPS_test(request):
    if request.method == 'POST':
        IPS_dto = l.create_IPS(json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto, ])
        return HttpResponse(ips, 'application/json')
    if request.method == 'PUT':
        if not(vl.validar(json.loads(request.body))):
                return HttpResponseBadRequest(HttpResponse("Error, invalid entry for update"))
        IPS_dto = l.update_IPS(1, json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto,])
        return HttpResponse(ips, 'application/json')

@csrf_exempt
def IPS_test_2(request):
    if request.mehtod == 'PUT':
        IPS_dto = l.update_IPS(1, json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto,])
        return HttpResponse(ips, 'application/json')
# Create your views here.