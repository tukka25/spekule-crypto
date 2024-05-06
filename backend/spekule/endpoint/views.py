from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tradingview_ta import TA_Handler, Interval, Exchange
from django.contrib.auth.models import User
import requests , re, json, random , string

@csrf_exempt
def Uniswap(request):
	if (request.method != "POST"):
		return (JsonResponse({'status':'unauthorized'}, status=401))

@csrf_exempt
def sayhello(request):
	if (request.method != "POST"):
		return (JsonResponse({'status':'Hello Ya Makna'}, status=200))

@csrf_exempt
def Jupiter(request):
	if (request.method != "POST"):
		return (JsonResponse({'status':'unauthorized'}, status=401))

@csrf_exempt
def tradingView(request):
	if (request.method != "POST"):
		return (JsonResponse({'status':'unauthorized'}, status=401))
	try:
		tesla = TA_Handler (
		symbol="ETH",
		screener="america",
		exchange="NASDAQ",
		interval=Interval.INTERVAL_1_DAY
		)
		print(tesla.get_analysis().summary)
		return (JsonResponse({'status':'success'}, status=200))
	except Exception as err:
		return (JsonResponse({'status': str(err)}, status=401))
