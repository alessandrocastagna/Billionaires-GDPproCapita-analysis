from bs4 import BeautifulSoup
import json
import pandas as pd
import requests
import math
import numpy as np
from scipy.stats import pearsonr

## Dataset related to bill characteristics from Forbes with API (true.json)
# source -> https://www.forbes.com
requestUrl = "https://www.forbes.com/forbesapi/person/rtb/0/-estWorthPrev/true.json?fields=uri,rank,listUri,finalWorth,personName,city,source,industries,countryOfCitizenship,imageExists,gender,birthDate,lastName,wealthList,estWorthPrev,familyList,squareImage,bioSuppress"
requestHeaders = {
"Accept": "application/json"
  }
response = requests.get(requestUrl, headers=requestHeaders)
category_list=json.loads(response.text)
category_list=category_list['personList']['personsLists'] 


## Dataset related to world countries per capita GDP
# source -> https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG
world_GDP = pd.read_csv("original_data/world_GDP.csv")
world_GDP=world_GDP[['Country Name','2014','2015','2016','2017','2018','2019','2020','2021']]
print(f"world_GDP\n{world_GDP.head(7)}\n")


## Dataset related to European Regional and Provincial per capita GDP
# source -> https://ec.europa.eu/eurostat/databrowser/view/nama_10r_2gvagr/default/table?lang=en
region_GDP = pd.read_csv("original_data/european_GDP_procapite.csv")
region_GDP = region_GDP[['TIME', '2014','2015','2016','2017','2018','2019','2020','2021']][1:]
print(f"region_GDP\n{region_GDP.head(7)}\n")


## Dataset related to American GDP
# source -> https://apps.bea.gov/itable/?ReqID=70&step=1&acrdn=1#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyNCwyOSwyNSwzMV0sImRhdGEiOltbIlRhYmxlSWQiLCI2MDAiXSxbIkNsYXNzaWZpY2F0aW9uIiwiTm9uLUluZHVzdHJ5Il0sWyJNYWpvcl9BcmVhIiwiMCJdXX0=
USA_GDP = pd.read_csv("original_data/US_states_GDP.csv")
USA_GDP=USA_GDP.drop(['GeoFips'], axis=1)
USA_GDP

## Dataset related to worth bill values with scraping from Forbes (all_worth_trend_bill.json)
with open('exported_data/all_worth_trend_bill.json', 'r', encoding='utf-8') as f:

    worth_trend = json.load(f)
# first ten elements of the billionaires worth trend list
cont = 0
print("all_worth_trend_bill\n")
for el in worth_trend:
    if cont <= 6:
        print(el,worth_trend[el])
        cont += 1
print("\n")


## Dataset related to American bill (american_bill_byProvince.json)
with open('exported_data/american_bill_byProvince.json', 'r', encoding='utf-8') as f:

    american_bill_byProvince = json.load(f)
# first ten elements of the billionaires
cont = 0
print("american_bill_byProvince\n")
for el in american_bill_byProvince:
    if cont <= 6:
        print(f"{el},{american_bill_byProvince[el]}")
        cont += 1
print("\n")


## Dataset related to European bill with scraping (european_bill_byProvince.json)
with open('exported_data/european_bill_byProvince.json', 'r', encoding='utf-8') as f:

    european_bill_byProvince = json.load(f)
# first ten elements of the billionaires 
cont = 0
print("european_bill_byProvince\n")
for el in european_bill_byProvince:
    if cont <= 6:
        print(f"{el},{european_bill_byProvince[el]}")
        cont += 1
print("\n")
