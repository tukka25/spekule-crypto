from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
	path("sayhello", views.sayhello, name="sayhello"),
	path("uniswap", views.Uniswap, name="uniswap"),
	path("jupiter", views.Jupiter, name="jupiter"),
	path("tradingView", views.tradingView, name="tradingView"),
	path("dexScreener", views.dexScreener, name="dexScreener"),
	# path("authenticate/", views.authenticateUser, name="authenticateUser"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
