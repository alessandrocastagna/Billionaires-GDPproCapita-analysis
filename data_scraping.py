from bs4 import BeautifulSoup
import json
import pandas as pd
import requests
import math
import numpy as np
from scipy.stats import pearsonr
from data_acquisition import *

# Dataset related to worth bill values with scraping from Forbes (all_worth_trend_bill.json)
url = "https://www.forbes.com/profile/"
worth_trend = {}

for el in category_list:
    
    r = requests.get(url+el['uri'])
    soup = BeautifulSoup(r.content) # If this line causes an error, run 'pip install html5lib' or install html5lib
    canvas_list = soup.find_all("canvas")
        
    for i in list(canvas_list):
        json_data = json.loads(i['data-chart'])
        bill_diz = {}
        for data in json_data:
            
            index = data['date'].find(" ")
            year = data['date'][index+1:]
            def_worth = data['worth'].replace("$","")
            def_worth = def_worth.replace("B","")
            
            if int(year) >= 2014 and int(year) <= 2022:
                bill_diz[int(year)] = float(def_worth)
        print(f"{el['personName']}-->{bill_diz}")
        
        worth_trend[el['personName']] = bill_diz
worth_trend

# Dataset related to American bill (american_bill_byProvince.json)
cont = 0
american_bill_byProvince = {}

for el in category_list:
    try:
        if el['state']!= None:
            if len(USA_GDP[USA_GDP['GeoName'] == el['state']])>0:
                american_bill_byProvince[el['personName']] = el['state']
    except KeyError:
        continue 
american_bill_byProvince  


## Dataset related to European bill with scraping (european_bill_byProvince.json)
### LIST CREATION OF THE EUROPEAN BILLIONAIRES

new_list = []
url = "https://www.geonames.org/search.html?q="

country_world = pd.read_csv("original_data/countries and continents.csv") # to check if a country is European
country_world = country_world[["name","Continent"]]

european_bill_byProvince = {}

for el in category_list:
    try:
        r = requests.get(url+el['city']+"&country=")
        soup = BeautifulSoup(r.content)
        row = soup.find_all('td')
        
        if len(row)>=6:
            path = row[5].get_text(separator=' ')
            
            residence_city = path.split(',')[0]
            print(f"{el['personName']}-->{residence_city.strip()}")
            continent = country_world[country_world['name']==residence_city.strip()]
            if len(continent)>0:
                if continent['Continent'].item()=="EU":
                    state = path.split(',')[0]
                    path = path.split(',')[1]
                    path = path.split('>')[0]
                    #path = path.split(' ')[1]
                    print(f"-->{el['personName']}-->{path}-->{state}")
                    european_bill_byProvince[el['personName']] = path
                
    except KeyError:   
        continue
        
european_bill_byProvince