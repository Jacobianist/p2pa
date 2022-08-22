from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import SimpsonQuote, BrBadQuote
from .serializers import SimpsonQuoteSerializer, LastQuoteSerializer, BrBaQuoteSerializer, LastBrBaQuoteSerializer
import requests


@api_view(['GET'])
def getData(request):
    data = []
    item = SimpsonQuote.objects.all().order_by('-created')[:1]
    serializer = LastQuoteSerializer(item, many=True)
    data.append(serializer.data)
    item2 = BrBadQuote.objects.all().order_by('-created')[:1]
    serializer2 = LastBrBaQuoteSerializer(item2, many=True)
    data.append(serializer2.data)
    return Response({"data": data})


# @api_view(['POST'])
def addQuote(request):
    sim = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    # r = [{
    #     "quote": "But my mom says I'm cool.",
    #     "character": "Milhouse Van Houten",
    #     "image":
    #     "https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FMilhouseVanHouten.png?1497567513002",
    #     "characterDirection": "Right"
    # }]

    serializer = SimpsonQuoteSerializer(data=sim.json(), many=True)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
    brba = requests.get("https://www.breakingbadapi.com/api/quote/random")
    serializer = BrBaQuoteSerializer(data=brba.json(), many=True)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()

    return HttpResponse(sim.json())  # .json()
