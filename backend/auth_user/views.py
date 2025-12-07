from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import auth_serializer,login_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt
def register(request):
    print('hello')
    if request.method == 'POST':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = auth_serializer(data=py_data)
        print(de_ser.is_valid())
        if de_ser.is_valid():
            de_ser.save()
            json_data = JSONRenderer().render({'msg':'registrations successfull'})
            return HttpResponse(json_data, content_type='application/json')
@csrf_exempt
def login_(request):
    print('heelo')
    if request.method == 'POST':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = login_serializer(data = py_data)
        if de_ser.is_valid():
            username = de_ser.validated_data['username']
            password = de_ser.validated_data['password']

            u = authenticate(username=username, password=password)
            if u:
                login(request, u)
                resp_data = JSONRenderer().render({'msg':'user loged in successfully'})
                return HttpResponse(resp_data)
def logout_(request):
    if request.method == 'GET':
        logout(request)
        resp_data = JSONRenderer().render({'msg':'logged out successfully'})
        return HttpResponse(resp_data)

