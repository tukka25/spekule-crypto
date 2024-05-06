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
from tradingview_ta import *
from django.contrib.auth.models import User
from .tradingViewUtils import Interval
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
		body_json = json.loads(request.body)
		# print(f"body = {len(body_json)}")
		if (len(body_json) != 4):
			return (JsonResponse({'status' : '4 arguments should be sent'}, status=400))
		req_symbol = body_json["symbol"]
		print(f"symbols = {req_symbol}")
		req_screener = body_json["screener"]
		req_exchange = body_json["exchange"]
		req_interval = body_json["interval"]
		print(f"interval = {req_interval}")
		if (Interval.get_interval(req_interval) == ""):
			return (JsonResponse({'status': 'Unknown Interval'}, status=400))
		# if (len(req_symbol) > 1):
		# 	analysis = get_multiple_analysis(screener=req_screener, interval=req_interval, symbols=req_symbol)
		tesla = TA_Handler (
			symbol=req_symbol,
			screener=req_screener,
			exchange=req_exchange,
			interval=req_interval
		)
		print(tesla.get_analysis().summary)
		return (JsonResponse({'status':'success', 'summary': tesla.get_analysis().summary}, status=200))
	except Exception as err:
		print(str(err))
		return (JsonResponse({'status': str(err)}, status=401))
