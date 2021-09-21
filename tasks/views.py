from todo import tasks
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import task

def taskList(request):
    tasks = task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def helloworld(request):
    return HttpResponse('Hello World !')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

