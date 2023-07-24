from data_acquisition import *

## Dataset related to world countries per capita GDP (world_GDP.csv)
# ROUND THE WORLD PRO CAPITA GDP AT TWO DECIMAL NUMBERS
for j in world_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
    list=[]
    for i in world_GDP[j]:
        list.append(round(float(i), 2))
            
    world_GDP[j]=list

# Country removing if there are all missing values for GDP from 2014 to 2021 and mean replacement for that countries which have at least one missing value but not all, must be 1 or more not null value.
df=pd.read_csv("original_data/world_GDP.csv")
lista=[]
for i in df.iterrows():
    if i[1]['2014']>=2 and i[1]['2015']>=2 and i[1]['2016']>=2 and i[1]['2017']>=2 and i[1]['2018']>=2 and i[1]['2019']>=2 and i[1]['2020']>=2 and i[1]['2021']>=2:
        lista.append({"Country Name":i[1]['Country Name'], "2014":i[1]['2014'], "2015":i[1]['2015'], "2016":i[1]['2016'], "2017":i[1]['2017'] ,"2018":i[1]['2018'] ,"2019":i[1]['2019'],"2020":i[1]['2020'], "2021":i[1]['2021'],})
    else:
        if i[1]['2014']>=2 or i[1]['2015']>=2 or i[1]['2016']>=2 or i[1]['2017']>=2 or i[1]['2018']>=2 or i[1]['2019']>=2 or i[1]['2020']>=2 or i[1]['2021']>=2:
            lista_valori = [i[1]['2014'],i[1]['2015'],i[1]['2016'],i[1]['2017'],i[1]['2018'],i[1]['2019'],i[1]['2020'],i[1]['2021']]
            media = np.mean([valore for valore in lista_valori if valore>2])
            lista_valori_sostituiti = pd.Series(lista_valori).fillna(media).tolist()
            lista.append({"Country Name":i[1]['Country Name'], "2014":lista_valori_sostituiti[0],"2015":lista_valori_sostituiti[1],"2016":lista_valori_sostituiti[2],"2017":lista_valori_sostituiti[3],"2018":lista_valori_sostituiti[4],"2019":lista_valori_sostituiti[5],"2020":lista_valori_sostituiti[6],"2021":lista_valori_sostituiti[7]})


## Dataset related to American countries GDP (US_GDP.csv)
# source -> https://www.census.gov/en.html
USA_POP = pd.read_csv("original_data/population_us.csv")
print(f"USA_POP\n{USA_POP.head(7)}\n")

# From GDP to GDP per capita by dividing each value with the population of the year 2022.
for j in USA_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
    list=[]
    cont = 0
    for i in USA_GDP[j]:
        pop = USA_POP.iloc[cont]['2022_population']
        pop = pop.strip()        
        pop = pop.replace(",","")
        pop = pop.rstrip('.00')
        gdp_proCapite = round(float(i) / float(pop) * 1000000.0, 2)
        print(f"GDP: {gdp_proCapite} -> {float(i)}-->{j}>>>population:{float(pop)}")
        list.append(gdp_proCapite)
        cont += 1
    USA_GDP[j]=list


## Dataset related to European countries GDP (European_GDP_procapite.csv)
# HERE THE EUROPEAN PRO CAPITA GDP CURRENCY IS TRANSLATED FROM EURO INTO USD AT CURRENT CHANGE VALUE
change_val = 1.0804
cont = 1

for j in region_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
    list=[]
    for i in region_GDP[j]:
        tmp=i.replace(',','.')
        #print(round(float(i)*1000.0, 2))
        if tmp.strip() != ':':
            list.append(round(float(tmp)*1000.0, 2))
        else:
            list.append(0.0)
            
    region_GDP[j]=list

# HERE THE EUROPEAN PRO CAPITA GDP CURRENCY IS TRANSLATED FROM THOUSANDS OF USD TO USD
for j in region_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
    list=[]
    for i in region_GDP[j]:
        if i==':':
            i=i.replace(i,'0')
            list.append(i)
        else:
            i=i*change_val
            list.append(i)
    
    region_GDP[j]=list

# mean replacement of null values
lista=[]
for i in region_GDP.iterrows():
    if i[1]['2014']>=2 and i[1]['2015']>=2 and i[1]['2016']>=2 and i[1]['2017']>=2 and i[1]['2018']>=2 and i[1]['2019']>=2 and i[1]['2020']>=2 and i[1]['2021']>=2:
        lista.append({"Country Name":i[1]['TIME'], "2014":i[1]['2014'], "2015":i[1]['2015'], "2016":i[1]['2016'], "2017":i[1]['2017'] ,"2018":i[1]['2018'] ,"2019":i[1]['2019'],"2020":i[1]['2020'], "2021":i[1]['2021'],})        
    else:
        if i[1]['2014']>=2 or i[1]['2015']>=2 or i[1]['2016']>=2 or i[1]['2017']>=2 or i[1]['2018']>=2 or i[1]['2019']>=2 or i[1]['2020']>=2 or i[1]['2021']>=2:
            lista_valori = [i[1]['2014'],i[1]['2015'],i[1]['2016'],i[1]['2017'],i[1]['2018'],i[1]['2019'],i[1]['2020'],i[1]['2021']]
            media = np.mean([valore for valore in lista_valori if valore>2])
            lista_valori_sostituiti = pd.Series(lista_valori).fillna(media).tolist()
            lista.append({"Country Name":i[1]['TIME'], "2014":lista_valori_sostituiti[0],"2015":lista_valori_sostituiti[1],"2016":lista_valori_sostituiti[2],"2017":lista_valori_sostituiti[3],"2018":lista_valori_sostituiti[4],"2019":lista_valori_sostituiti[5],"2020":lista_valori_sostituiti[6],"2021":lista_valori_sostituiti[7]})

