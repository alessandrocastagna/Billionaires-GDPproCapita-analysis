from data_cleaned_enriched_import import category_list,worth_trend,american_bill_byProvince,european_bill_byProvince,eur_matched
import json

## COUNTING HOW MANY BILLIONAIRES HAVE NO RESIDENCE CONTINENT
cont = 0 

for el in category_list:
    try:
        if el['continent'] == '':
            cont += 1
    except KeyError:
        continue
print(f"{cont} null values of continent in the enriched true json")


## COUNTING HOW MANY BILLIONAIRES HAVE NO WORTH TREND IN THE PERIOD UNDER STUDY

cont_eu = 0
cont_us = 0
cont_null_eu = 0
cont_null_us = 0

for el in worth_trend:
    if el in american_bill_byProvince:
        cont_us += 1
        if len(worth_trend[el]) == 0:
            cont_null_us += 1
    if el in european_bill_byProvince:
        cont_eu += 1
        if len(worth_trend[el]) == 0:
            cont_null_eu += 1
print(f"{cont_eu} vs {cont_null_eu} : {cont_eu - cont_null_eu} european scraped in the european_bill_byProvince.json")
print(f"{cont_us} vs {cont_null_us} : {cont_us - cont_null_us} us scraped in the american_bill_byProvince.json")

## Missing values of eur_prov_matched_bill.json
for el in eur_matched:
    if el['region'] != '' and european_bill_byProvince[el['nome']].strip()!='Moscow':
        cont+=1
print(f"{len(european_bill_byProvince)} vs {cont} : {(len(european_bill_byProvince)) - cont} not matched in the eur_prov_matched_bill.json")

## Missing values of the merged dataset in MongoDB
with open('./final_data/Final_Dataset.json', 'r', encoding='utf-8') as f:
    final = json.load(f)

cont = 0
for el in final:
    if len(el['bill_worth'])==0:
        cont += 1
print(f"{cont} European and American billionaires have no worth trend")
