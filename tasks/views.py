from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TaskSerializer
from django.core import serializers


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def tasks(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize("json", tasks)
    return HttpResponse(tasks_json ,content_type="application/json")

def add(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data, status=201)
        
    return HttpResponse(serializer.errors, status=404)
