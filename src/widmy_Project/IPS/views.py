from django.shortcuts import render
from .logic import IPS_logic as l
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def IPSs_view(request):
    if request.method=='GET':
        id = request.GET.get("id",None)
        if id:
            IPS_dto = l.get_IPS(id)
            ips = serializers.serialize('json',[IPS_dto,])
            return HttpResponse(ips, 'application/json')
        else:
            IPSs_dto = l.get_IPSs()
            print("EXPLOLTA AQUI")
            IPSs = serializers.serialize('json', IPSs_dto)
            return HttpResponse(IPSs, 'application/json')
    if request.method == 'POST':
        IPS_dto = l.create_IPS(json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto, ])
        return HttpResponse(ips, 'application/json')

@csrf_exempt
def IPS_view(request, pk):
    if request.method == 'GET':
        IPS_dto = l.get_IPS(pk)
        ips = serializers.serialize('json', [IPS_dto,])
        return HttpResponse(ips, 'application/json')
    if request.method == 'PUT':
        IPS_dto = l.update_IPS(pk, json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto,])
        return HttpResponse(ips, 'application/json')
    if request.method == 'DELETE':
        IPS_dto = l.delete_IPS(pk, json.loads(request.body))
        ips = serializers.serialize('json', [IPS_dto,])
        return HttpResponse(ips, 'application/json')

# Create your views here.
