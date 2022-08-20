from django.shortcuts import render
from . import pyspotipy
from django.http import JsonResponse
# Create your views here.


def post_list(request):
  bill=pyspotipy.billboardpy.get_all_years()
  return JsonResponse(bill, safe=False)
  
def get_months(request,year):
  months=pyspotipy.billboardpy.get_months(year)
  return JsonResponse(months,safe=False)
  
def get_hot_100(request,month):
  hot_100=pyspotipy.billboardpy.get_hot_100(month)
  return JsonResponse(hot_100, safe=False)
  
def get_current_100(request):
  bill=pyspotipy.billboardpy.get_current_100()
  return JsonResponse(bill, safe=False)
  
def get_url(request,track,artist):
  url=pyspotipy.search_song(track,artist)
  return JsonResponse(url, safe=False)
  