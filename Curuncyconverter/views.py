from django.http import HttpResponse
from django.shortcuts import render
from . import cron

def index(request):
    return render(request,'index.html')

def curency_convert(request):
    curency=request.GET.get('curency')
    amount=request.GET.get('INR')
    cron.fetch_data()
    a=cron.calc(curency,amount)
    params={'curency':curency , 'amount':round(a,3)}
    return render(request,'index.html',params)
