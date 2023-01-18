import ast
from django.shortcuts import render
import json
import requests
import pandas as pd
from  .models import *

# Create your views here.

    
def ul(request):
    return render(request, 'u.html')

def two(request):
    data = open(r'C:\Users\VChougani\Desktop\sample1\a.json').read()
    json_data = json.loads(data)
    return render(request,'two.html',{"json_data" : json_data})
    
def demand(request):
    response = requests.get('http://10.11.52.113:1000/dee')
    r2 = response.json()
    demand_df = pd.DataFrame.from_dict(r2)
    print(demand_df)
    context = {
         'df' : demand_df.to_html()
        }
    return render(request,'demand.html',context)

def supply(request):
    data = open(r'C:\Users\VChougani\Desktop\sample1\a.json').read()
    json_data = json.loads(data)
    response = requests.get('http://10.11.52.113:2000/',json = json_data)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context = {
         'df' : supply_df.to_html()
        }
    return render(request,'supply.html',context)

# def one(request):
#     URL = "http://10.11.52.113:2000/"
#     Demand = input("Enter a demand:")
#     # params = int(request.GET.get('demand'))
#     # response = requests.get('http://10.11.52.113:2000/',json = params)
#     data = requests.get(URL + Demand)
#     data = data.json()
#     try:
#         data_json = json.loads(data)
#         print(data_json)

#     except json.JSONDecodeError:
#         print("Empty response ")
#     supply_df = pd.DataFrame.from_dict(data_json)
#     print(supply_df)
#     context = {
#          'df' : supply_df.to_html()
#         }
#     return render(requests.request,'one.html',context)
# if __name__ == "__one__":
#     one()

    # r3 = response.json()
    # dict = pd.json_normalize(response)
    # print(dict)
   

def index(request):
    return render(request, 'a.html')

def three(request):
    params = {"demand" : 9}
    json_data = json.dumps(params)
    return render(request,'three.html',{"json_data" : json_data})

# def getdemand(request):
#     demand=demands.objects.filter(demand_id=request.)

# def alert_data(demand):
# {
def one(request):
    URL = "http://10.11.52.113:2000/"
    Demand = input("Enter a demand:")
    # params = int(request.GET.get('demand'))
    # response = requests.get('http://10.11.52.113:2000/',json = params)
    response = requests.get(URL , Demand)
    r3 = response.json()
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context = {
         'df' : supply_df.to_html()
        }
    return render(request,'one.html',context)

#     return alert('demand': + 'number')
# {
#     "demand" : "$input.params('demand')"
# }

