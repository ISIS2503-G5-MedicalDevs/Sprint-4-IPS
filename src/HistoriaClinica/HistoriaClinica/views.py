from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rset_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId




@api_view(["GET","POST"])
def HistoriasClinicas_view(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.hc_db
    hcs = db['HistoriasClinicas']
    if request.method == 'GET':
        result =[]
        data = hcs.find({})
        for dto in data:
            jsonData = {
                'id' : str(dto['_id']),
                'motivoConsulta' : dto['motivoConsulta'],
                'enfermedadActual' : dto['EnfermedadActual'],
                'analisis' : dto['analisis'],
                'diagnostico' : dto['diagnostico'],
                'procedimiento': dto['procedimiento'],
                'fecha' : dto['fecha'],
                'hora' : dto['hora']
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = hcs.insert(data)
        respo = {
            "MongoObjectID" : str(result),
            "Message": "nueva historia clinica registrada en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)

@api_view(["GET"])
def HistoriaClinica_view(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.hc_db
    hcs = db['HistoriasClinicas']
    if request.method == 'GET':
        data = hcs.find({'_id': ObjectId(pk)})
        result = []
        for dto in data:
            jsonData = {
                'id' : str(dto['_id']),
                'motivoConsulta' : dto['motivoConsulta'],
                'enfermedadActual' : dto['EnfermedadActual'],
                'analisis' : dto['analisis'],
                'diagnostico' : dto['diagnostico'],
                'procedimiento': dto['procedimiento'],
                'fecha' : dto['fecha'],
                'hora' : dto['hora']
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result[0], safe = False)