from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView,View
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import json

class jsonView(APIView):
    
    def get(self, request):

        return Response({"slackUsername": "saeeda06", "backend": True, "age": 28, "bio": "i am a backend developer"})


