from django.shortcuts import render
from django.http import HttpResponse
from .models import taskmodel
from .serializer import taskserializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@ csrf_exempt
def tasks(request,pk):
    if request.method == 'GET':
        model_instance = taskmodel.objects.filter(Q(is_del = False)& Q(is_comp = False) & Q(host=pk))
        ser_data = taskserializer(model_instance,many=True)
        py_data = ser_data.data
        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data)
    if request.method == 'POST':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = taskserializer(data = py_data)
        if de_ser.is_valid():
            de_ser.save()
            json_data = JSONRenderer().render({'msg':'the data created successfully'})
            return HttpResponse(json_data)
    
@ csrf_exempt
def update_task(request,pk):
    try:
        model_instence = taskmodel.objects.get(id=pk)
    except:
        json_data= JSONRenderer().render({'msg': 'data is not available in the backend'})
        return HttpResponse(json_data)

    if request.method == 'GET':
        ser_py = taskserializer(model_instence)
        py_data = ser_py.data
        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data)
    
    if request.method == 'PUT':
        req_data = request.body
        stream_data =io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = taskserializer(model_instence,data=py_data, partial = True)
        
       
        if de_ser.is_valid():
            print('data received')
            de_ser.save()
            json_data= JSONRenderer().render({'msg': 'data updated in the backend'})
            return HttpResponse(json_data)
    if request.method == 'DELETE':
        model_instence.is_del= True
        model_instence.save()
        json_data = JSONRenderer().render({'msg':'data got deleted from the backend'})
        return HttpResponse(json_data)

def history(request,pk):
    if request.method == 'GET':
        model_instance = taskmodel.objects.filter(Q(is_del = True) & Q(host=pk))
        ser_data = taskserializer(model_instance,many=True)
        py_data = ser_data.data
        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data)

def restore(request,pk):
    model_instance = taskmodel.objects.get(id = pk)
    if request.method == 'GET':
        model_instance.is_del = False
        model_instance.save()
        json_data = JSONRenderer().render({'msg':'data got restored to the backend'})
        return HttpResponse(json_data)

@ csrf_exempt
def delete_all(request):
    model_instance = taskmodel.objects.filter(is_del= True)
    if request.method == 'DELETE':
        model_instance.delete()
        json_data = JSONRenderer().render({'msg':'NO data in history'})
        return HttpResponse(json_data)
    if request.method == 'GET':
        for i in model_instance:
            i.is_del = False
            i.save()
        json_data = JSONRenderer().render({'msg':'all the data got restored to the backend'})
        return HttpResponse(json_data)

@ csrf_exempt
def del_hist(request,pk):
    print('hello')
    model_instance= taskmodel.objects.get(id = pk)
    if request.method == 'DELETE':
        model_instance.delete()
        json_data = JSONRenderer().render({'msg':'the data got delete permenently'})
        return HttpResponse(json_data)
@csrf_exempt
def completed_task(request,pk):
    model_instance = taskmodel.objects.get(id = pk)
    if request.method == 'GET':
        if model_instance.is_comp == False:
            model_instance.is_comp = True
            model_instance.save()
            resp_data = JSONRenderer().render({'msg':'Task completed successfully'})
            return HttpResponse(resp_data)
        else:
            model_instance.is_comp = False
            model_instance.save()
            resp_data = JSONRenderer().render({'msg':'Task is Uncompleted'})
            return HttpResponse(resp_data)
def completed_page(request,pk):
    if request.method == 'GET':
        model_instance = taskmodel.objects.filter(Q(is_del = False) & Q(is_comp = True) & Q(host=pk))
        ser_data = taskserializer(model_instance,many=True)
        py_data = ser_data.data
        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data)