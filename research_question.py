import json
import numpy as np
import pandas as pd
from scipy.stats import pearsonr

# All the datasets have been aggregated into the Final_Dataset.json. For further information you can look at the report.

with open("final_data/Final_Dataset.json", encoding="utf-8") as f:
    
    Final= json.load(f)

## Question 1:
# Do countries with more billionaires, in US and Europe, actually have a higher Gross Domestic Product 
# on average than other countries?

diz={}
for i  in Final:
    if i['residence_state'] not in diz:
        diz[i['residence_state']]=1
    else:
        diz[i['residence_state']]+=1

        
final_diz={}
for i in Final:  
    momentaneo=[]
    for j in i['state_GDP'][0]:
        if j[0]=='2':
            momentaneo.append(i['state_GDP'][0][j])
    
    final_diz[i['state_GDP'][0]['Country Name']]=np.mean(momentaneo)

sort=sorted(diz.items(),key=lambda x: x[1],reverse=True)
query1={}
for i in sort:
    for j in final_diz:
        if i[0]==j:
            query1[j]=final_diz[j]
Country_Name=[i for i in query1.keys()]
Mean_GDP=[i for i in query1.values()]
n_bill=[]
for i in sort:
    n_bill.append(i[1])

data={'N_Billionaire':n_bill, 'Country_Name': Country_Name, 'Mean_GDP':Mean_GDP}
df = pd.DataFrame(data)
print(df)

## Question 2:
# Which is/are the billionaire/billionaires, in US and Europe, with the highest correlation between his/her/them worth 
# trends and GDP trends in the european region/european province/US state?


pearson_corr={}
for i in Final:
    diz_country={}
    diz_bill={}
    if i['bill_worth']!=[] and len(i['bill_worth'][0])>=5 and i['state/region_GDP']!=[] and len(i['state/region_GDP'][0])>=4: # ci sono paesi come russia e bill senza worth
        for j in i['state/region_GDP'][0]:
            if j[0]=='2':
                diz_country[j]=i['state/region_GDP'][0][j]
        for t in i['bill_worth'][0]:
            if t[0]=='2':
                diz_bill[t]=i['bill_worth'][0][t]                
        new_country_diz={}
        for k, v in diz_country.items():
            if k in diz_bill:
                new_country_diz[k]=v
        x=[i for i in new_country_diz.values()]
        y=[i for i in diz_bill.values()]
        pearson_corr[i['personName']] = pearsonr(x, y)[0]
        
sort=sorted(pearson_corr.items(),key=lambda x: x[1],reverse=True)
bill=[]
correaltion=[]
for i in sort:
    bill.append(i[0])
    correaltion.append(i[1])

data={'Billionaire':bill, 'Pearson correaltion': correaltion}
df = pd.DataFrame(data)
print(df[0:10])
print(df[776:])
    

#focus on the max correlation value
massimo=max(pearson_corr.values())
lista_massimo={}
for i in pearson_corr:
    if pearson_corr[i]==massimo:
        lista_massimo[i]=pearson_corr[i]
         
country=[j['state/region_GDP'][0]['Country Name'] for j in Final if j['personName']==i]
bill=[i for i in lista_massimo.keys()]
                 
diz_GDP={}
diz_country={}    
new_GDP_diz={}
diz_bill_trend={}
for i in Final:
    if i['personName']==bill[0]:  
        for j in i['state/region_GDP'][0]:
            if j[0]=='2':
                diz_country[j]=i['state/region_GDP'][0][j]
        for t in i['bill_worth'][0]:
                if t[0]=='2':
                    diz_bill_trend[t]=i['bill_worth'][0][t]                
        for k, v in diz_country.items():
            if k in diz_bill_trend:
                new_GDP_diz[k]=v
                    
print(f"The most influential billionaire is {bill[0]}, with a correlation value of his worth and the Gross Domestic Product of his country ({country[0]}) of {round(massimo,6)}.")
print(f"This correlation coefficient is based on the following values:")
print(f"1) Gross Domestic Product of {country[0]}: {new_GDP_diz}.")
print(f"2) {bill[0]}'s worth trend: {diz_bill_trend} (each values is expres in billions of dollars).")

## Question 3:
# In the top 10 richest countries (with the highest average GDP) in US and Europe, what percentage of billionaires are 
# women?

   
top={}
for i in Final:
    lista=[]
    if i['state_GDP']!=[]:
        for j in i['state_GDP'][0]:
                if j[0]=='2':
                    lista.append(i['state_GDP'][0][j])
    top[i['residence_state']]=np.mean(lista)


countryF={}
countryM={}
country={}
for i in Final:
    if i['residence_state'] not in country:
        country[i['residence_state']]=1
    else:
        country[i['residence_state']]+=1
            
    if i['gender']=='F':
        if i['residence_state'] not in countryF:
            countryF[i['residence_state']]=1
        else:
            countryF[i['residence_state']]+=1    
            
for i in country.keys():
    if i not in countryF.keys():
        countryF[i]=0        
            
            
sort=sorted(top.items(),key=lambda x: x[1],reverse=True)
state=[i[0] for i in sort]
average_GDP=[round(i[1],2) for i in sort]
percentage=[round((countryF[i]/country[i])*100,2) for i in state]

countryF = dict(sorted(countryF.items(), key=lambda x: state.index(x[0])))
country = dict(sorted(country.items(), key=lambda x: state.index(x[0])))


data={'State':state, 'Average GDP per capita':average_GDP,'Women percentage':percentage, 'N women billionaire': countryF.values(),'N billionaire': country.values()}
df = pd.DataFrame(data)
df=df[0:10]
print(df)
