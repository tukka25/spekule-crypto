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
from uniswap import Uniswap
from .dexScreenerUtils import get_token_addresses
from dexscreener import DexscreenerClient


@csrf_exempt
def Uniswap(request):
	if (request.method != "POST"):
		return (JsonResponse({'status':'unauthorized'}, status=401))
	try:
		address = None         # or None if you're not going to make transactions
		private_key = None  # or None if you're not going to make transactions
		version = 2                       # specify which version of Uniswap to use
		provider = "https://mainnet.infura.io/v3/7991dcb56e4447e7bf1b25fa5a18c17f"    # can also be set through the environment variable `PROVIDER`
		uniswap = Uniswap(request=request, address=address, private_key=private_key, version=version, provider=provider)

		# Some token addresses we'll be using later in this guide
		eth = "0x0000000000000000000000000000000000000000"
		bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
		dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
		return (JsonResponse({'status': 'All Good'}, status=200))
	except Exception as err:
		print(str(err))
		return (JsonResponse({'status': str(err)}, status=400))

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

@csrf_exempt
def dexScreener(request):
	my_dict = {}
	if (request.method != "POST"):
		return (JsonResponse({'status':'unauthorized'}, status=401))
	try:
		body_json = json.loads(request.body)
		print(f"body = {len(body_json)}")
		if (len(body_json) != 1):
			return (JsonResponse({'status' : '1 argument should be sent'}, status=400))
		fulltoken = body_json["token"]
		print(f"{fulltoken}")
		tt = fulltoken.split("/")
		if (len(tt) == 1):
			print("here")
			url = "https://api.dexscreener.io/latest/dex/tokens/" + tt[0]
			print(f"url = {url}")
		else:
			print("here2")
			if (len(tt) != 2 or tt[1] == "" or tt[0] == ""):
				return (JsonResponse({'status' : 'Invalid token'}, status=400))
			chain = tt[0]
			token = tt[1]
			url = "https://api.dexscreener.io/latest/dex/pairs/" + chain + "/" + token
			print(f"token = {token}, chain = {chain}")
		print(f"url = {url}")
		response = requests.get(url)
		print(response.status_code)
		if (response.status_code == 200):
			data = response.json()
			print(f"data = {data}")
			for pair in data['pairs']:
				txns = pair['txns']
				# print(f"txns = {txns}")
				for period, txn_data in txns.items():
					my_dict[period] = txn_data
					# my_dict[period] = txn_data
					print (f"period = {period}, buys = {txn_data['buys']}, sells = {txn_data['sells']}")
			# for key, value in my_dict.items():
			# 	dict[key] = dict(value)
			return (JsonResponse({'status': 'success', 'data': my_dict}, status=200))
		return (JsonResponse({'status': 'hello'}, status=400))
	except Exception as err:
		print(str(err))
		return (JsonResponse({'status': str(err)}, status=401))
	