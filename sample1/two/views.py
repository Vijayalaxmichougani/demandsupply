
from django.shortcuts import render,redirect
from django.forms import Form
import json
import requests
import pandas as pd
from  .models import *
from .forms import usersform

# Create your views here.

    
def ul(request):
    return render(request, 'u.html')

def two(request):
    response = requests.get('http://10.11.52.113:9000/demand_17')
    r2 = response.json()
    demand_df = pd.DataFrame.from_dict(r2)
    print(demand_df)
    context = {
        
         'df' : demand_df.to_html()
        
        }
    return render(request,'two.html',context)
    
def demand(request):
    response = requests.get('http://10.11.52.113:9000/demand_17')
    r2 = response.json()
    demand_df = pd.DataFrame.from_dict(r2)
    print(demand_df)

    num1 = int(request.GET["num1"])
    demand1 = {"demand" : num1}    
    response = requests.get('http://10.11.52.113:8000/sup_17',json = demand1)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context1 = {
        'demand' : num1,
         'df' : demand_df.to_html(),
         'df1' : supply_df.to_html()
        }
    return render(request,'demand.html', context1)


def supply(request):
    num2 = int(request.GET["num1"])
    demand1 = {"demand" : num2}
    URL = "http://10.11.52.113:8000/sup_17"
    response = requests.get(URL, json = demand1)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context = {
        'd' : num2,

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
    num1 = int(request.GET["num1"])
    demand1 = {"demand" : num1}    
    response = requests.get('http://10.11.52.113:8000/sup_17',json = demand1)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context1 = {
        
         'df1' : supply_df.to_html()
        }
    return render(request,'demand.html', context1)
def one(request):
    URL = "http://10.11.52.113:8000/sup_17"
    # demand1 = input("Enter resource demand: >")
    # Demand = {'demand' : }
    # header = {'Demand' : f'demand {final()}'}
    demand1 = final(demand)
    response = requests.get(URL, json=demand1)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context = {
         'df' : supply_df.to_html()
       
        }
    return render(request,'one.html',context)

def final(request):
    return render(request, "final.html")
    

def final1(request):
    num1 = int(request.GET["num1"])
    num2= int(request.GET["num2"])
    res = num1+num2
    return render(request,'final1.html', {"result": res})

def usersform(request):
    fn=usersform(request)
    data ={}
    try:

        if request.method == "POST":
            n1 =int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data = {
                
                'output':finalans
             } 
            url = "/?output={}".format(finalans)
            return redirect(url)
    except:
        pass      
    return render(request,'userform.html',data)