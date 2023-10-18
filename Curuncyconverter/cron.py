import requests
import time
import json
url="http://data.fixer.io/api/latest?access_key=6a6fec6c6d0efd917035b378fde538ee&base=EUR&symbols=INR,USD,JPY"
t=time.time()

def load_data():
    j=open('data.json','w')
    j.truncate()
    j.close()
    res=requests.get(url)
    with open('Curuncyconverter\data.json','w') as json:
        json.write(res.text)
    json.close()

def fetch_data():
    global t
    if time.time()>=t:
        load_data()
        t=time.time()+3600

with open("Curuncyconverter\data.json",'r') as f:
    js=json.load(f)
    inr=js['rates']['INR']

def toeuro(amount):
    return float(amount)/float(inr)

def calc(curency,amount):
    euro=toeuro(amount)
    if curency=="EUR":
        return euro 
    return float(js['rates'][curency])*euro


