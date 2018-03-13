from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests
from django.http import HttpResponse

YOUR_KEY = "ad78c75776b93da787d08df051b73e19"

class MusicSearch(APIView):
    def get(self, request, *args, **kwargs):
        if "search" in request.GET:
            search = request.GET.get("search")

            params={"method" : "track.search", "api_key": YOUR_KEY,"track" : search, "format" : "json"}

            req = requests.get("http://ws.audioscrobbler.com/2.0/", params=params)         
            print req.url
            res = json.loads(req.text)
            return Response(res)
        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)

class Test(APIView):
    def get(self, request, *args, **kwargs):
	if "hub.challenge" in request.GET:
	    return HttpResponse(request.GET.get("hub.challenge"))
