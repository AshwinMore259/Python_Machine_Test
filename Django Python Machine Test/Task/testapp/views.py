from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response

# Create your views here.
class CreateClient(APIView):
    def post(self,request):
        data = request.data
        serializer = ClientSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        else:
            return Response({"data":serializer.errors})
    def get(self,request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many = True)
        return Response({"data":serializer.data})
