from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pythonwhois
from django.http.response import HttpResponse
import requests
import json
import urllib2
import xmltodict
import sys

from bot.helpers import *

class HubChallenge(APIView):

    PAGE_ACCESS_TOKEN  = 'EAAdK4IfLTbQBAHJGvfx9e27RbVKQBsJRM4kUGAW3zZA43WrEpHBg11zht8m2FUSYRt9mqvfKCMiqRSi1pd5k7icKanm6KuCP6k90vNiObR0fTVBiICKNgxXb9rRYVL1VFsy4jmZBnkUKDY1HO1exZA2pin1FZBVJL2RVJSF95wZDZD'
    
    YOUR_BOOK_KEY = "z8BdUYyClBcYIiGglrXMBA"

    standard_greetings = ['hello', 'hi', 'hey', 'morning', 'good morning', 'hii', 'greetings']

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('hub.verify_token'):
            print self.request.GET['hub.verify_token']
            print self.request.GET['hub.challenge']
            return HttpResponse(self.request.GET['hub.challenge'])
        return Response({"Hello": "World"})

    def post(self, request, *args, **kwargs):

        webhook_event =  request.data['entry'][0]['messaging'][0]
        sender_psid = webhook_event['sender']['id']
        print sender_psid
        message = webhook_event.get('message')


        req = requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    json={
                    "access_token": self.PAGE_ACCESS_TOKEN,
                    "recipient": {"id": sender_psid},
                    "sender_action":"mark_seen",
                          })

        #Start typing action while response is being fetched and posted
        req = requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    json={
                    "access_token": self.PAGE_ACCESS_TOKEN,
                    "recipient": {"id": sender_psid},
                    "sender_action":"typing_on",
                          })

        res = ['', '']

        
        if message:
            text = message['text'].lower()
            if message['text'].lower() in self.standard_greetings:
                res = "{0} \nPlease enter a query to search.".format(message['text'].title())

            else:
                res = book_request_handler(text)
                
                if res[1]:
                    print res[1]
                    req = requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    json={
                        "access_token": self.PAGE_ACCESS_TOKEN,
                        "recipient": {"id": sender_psid},
                        "message": {
                            "attachment": {
                                "type":"image",
                                "payload": {
                                    "url" : res[1],
                                    "is_reusable":True }
                                    }
                            }
                          })

        response = {'text': res[0]}
        req = requests.post("https://graph.facebook.com/v2.6/me/messages", 
                    json={
                    "access_token": self.PAGE_ACCESS_TOKEN,
                    "recipient": {"id": sender_psid},
                    "message": response,
                          })
        
        
        return Response({'received data': request.data})
