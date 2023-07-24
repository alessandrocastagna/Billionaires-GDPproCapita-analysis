import json

with open('final_data/all_worth_trend_bill.json', 'r', encoding='utf-8') as f:

    all_worth_trend_bill = json.load(f) 
# first ten elements of the billionaires 
cont = 0
print("all_worth_trend_bill\n")
for el in all_worth_trend_bill:
    if cont <= 10:
        print(el)
        cont += 1
print("\n")

with open('final_data/american_bill_byProvince.json', 'r', encoding='utf-8') as f:

    american_bill_byProvince = json.load(f) 
# first ten elements of the billionaires 
cont = 0
print("american_bill_byProvince\n")
for el in american_bill_byProvince:
    if cont <= 10:
        print(el)
        cont += 1
print("\n")

with open('final_data/true.json', 'r', encoding='utf-8') as f:

    true = json.load(f) 
# first ten elements of the billionaires 
cont = 0
print("true\n")
for el in true:
    if cont <= 10:
        print(el)
        cont += 1
print("\n")

with open('final_data/US_states_GDP.json', 'r', encoding='utf-8') as f:

    US_states_GDP = json.load(f) 
# first ten elements of the billionaires 
cont = 0
print("US_states_GDP\n")
for el in US_states_GDP:
    if cont <= 10:
        print(el)
        cont += 1
print("\n")