from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import requests
import json
from django.http import HttpResponse

API_KEY = "040b462a3e46fe07c098aae8c0d806d6"

class MovieSearch(APIView):
    def get(self, request, *args, **kwargs):
        if "search" in request.GET:
            query = request.GET.get("search")
            req = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key":API_KEY,"query":query})
            res = json.loads(req.text)
            return Response(res)
        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)

class TVSearch(APIView):
    def get(self, request, *args, **kwargs):
        if "search" in request.GET:
            query = request.GET.get("search")
            req = requests.get("https://api.themoviedb.org/3/search/tv", params={"api_key":API_KEY,"query":query})
            res = json.loads(req.text)
            return Response(res)
        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)


