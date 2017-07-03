from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib2
import xmltodict
import json
import requests

YOUR_KEY = "z8BdUYyClBcYIiGglrXMBA"

class BookSearch(APIView):
    def get(self, request, *args, **kwargs):
        if "search" in request.GET:
            query = request.GET.get("search")

            req = requests.get("https://www.goodreads.com/search.xml", params={"key": YOUR_KEY,"q" : query})
            xml = req.text
            dict = xmltodict.parse(xml)
            res = {}
            len = int(dict["GoodreadsResponse"]['search']['results-end'])

            for i in range(len):

                book = dict["GoodreadsResponse"]['search']['results']['work'][i]
                book['best_book']['average_rating'] = book['average_rating']
                
                id= book['best_book']['id']['#text']
                book['best_book']['id'] = id
                author = book['best_book']['author']['name']
                book['best_book']['author'] = author
            
                title = 'book_%d_details'%i
                res[title] = book['best_book']
            return Response(res)
        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)
