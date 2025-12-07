from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request,pk):
    url = f'http://127.0.0.1:8000/api/tasks/{pk}/'
    resp = requests.get(url = url)
    return render(request,'home.html', {'data':resp.json()})
@login_required(login_url='login')
def add_task(request,pk):
    url = f'http://127.0.0.1:8000/api/tasks/{pk}/'
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']

        py_data = {
            'title':title,
            'desc':desc,
            'host': request.user.id
        }
        
        resp = requests.post(url=url, json=py_data)
        return redirect('home', request.user.id)
    return render(request, 'add_task.html')
@login_required(login_url='login')
def update(request,pk):
    url = f'http://127.0.0.1:8000/api/update_task/{pk}/'
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']

        py_data = {
            'title':title,
            'desc':desc
        }
        json_data = json.dumps(py_data)
        resp = requests.put(url=url,data=json_data)
        return redirect('home', request.user.id)
    if request.method == 'GET':
        url = f'http://127.0.0.1:8000/api/update_task/{pk}/'
        resp = requests.get(url)
    return render(request,'update.html',{'data':resp.json()})
def completed_task(request,pk):
    url = f'http://127.0.0.1:8000/api/completed_task/{pk}/'
    resp = requests.get(url=url)
    return redirect('completed_page', request.user.id)
def completed_page(request,pk):
    url = f'http://127.0.0.1:8000/api/completed_page/{pk}/'
    resp = requests.get(url=url)
    return render(request,'completed_page.html', {'data':resp.json()})
@login_required(login_url='login')
def delete_(request,pk):
    url = f'http://127.0.0.1:8000/api/update_task/{pk}/'
    resp = requests.delete(url)
    return redirect('history', request.user.id)
@login_required(login_url='login')
def history(request, pk):
    url = f'http://127.0.0.1:8000/api/history/{pk}/'
    resp = requests.get(url = url)
    return render(request,'history.html', {'data':resp.json()})
@login_required(login_url='login')
def restore(request,pk):
    url = f'http://127.0.0.1:8000/api/restore/{pk}/' 
    resp = requests.get(url=url)
    return redirect('home' , request.user.id)
def delete_all(request):
    print('hello') 
    url = f'http://127.0.0.1:8000/api/delete_all/'
    resp = requests.delete(url=url)
    return redirect('history', request.user.id)

def restore_all(request):
    url = f'http://127.0.0.1:8000/api/delete_all/'
    resp = requests.get(url=url)
    return redirect('home', request.user.id)

def del_hist(request,pk):
    print('hello world')
    url = f'http://127.0.0.1:8000/api/delete_hist/{pk}/'
    resp = requests.delete(url=url)
    return redirect('history', request.user.id)