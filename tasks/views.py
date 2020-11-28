from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.core import serializers
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def tasks(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize("json", tasks)
    return HttpResponse(tasks_json ,content_type="application/json")

@api_view(["POST"])
def add(request):
    dataJson = JSONParser().parse(request)
    serializer = TaskSerializer(data=dataJson)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(["DELETE"])
def delete(request):
    Task.objects.all().delete()
    return Response({"message": "All tasks deleted!"})
