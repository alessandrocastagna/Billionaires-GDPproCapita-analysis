from data_cleaned_enriched_import import *
from unidecode import unidecode

## Transformation of the file schema for mongo db uploading (eur_prov_matched_bill.json)
list=[]
for i in eur_matched:
        diz={}
        diz['nome']=i
        diz['region']=eur_matched[i]
        list.append(diz)

## Transformation of the file schema for mongo db uploading (all_worth_trend_bill.json)
#list of dictionaries and application of unidecode function for translate name with special character into a comparable one.

list=[]
for i in worth_trend:
    diz={}
    diz['nome']=i
    for j in worth_trend[i]:
        diz[j]=worth_trend[i][j]
    list.append(diz)

for i in list:
    i['nome']=unidecode(i['nome'])

## Transformation of the file schema for mongo db uploading (american_bill_byProvince.json)
list=[]
for i in american_bill_byProvince:
    diz={}
    diz['nome']=i
    diz['country']=american_bill_byProvince[i]
    list.append(diz)

## Transformation of the file schema for mongo db uploading (true.json)
for i in category_list:
    i['personName']=unidecode(i['personName'])

## Transformation of the file schema for mongo db uploading (US_states_GDP.json)
list=[]
for i in USA_GDP.iterrows():
    diz={}
    diz['Country Name']=i[1]['GeoName']
    diz['2014']=i[1]['2014']
    diz['2015']=i[1]['2015']
    diz['2016']=i[1]['2016']
    diz['2017']=i[1]['2017']
    diz['2018']=i[1]['2018']
    diz['2019']=i[1]['2019']
    diz['2020']=i[1]['2020']
    diz['2021']=i[1]['2021']
    list.append(diz)
    