from data_acquisition import *

## Dataset related to bill characteristics (True.json)
# TRUE.JSON INTEGRATION WITH CONTINENT AND RESIDENCE STATE OF THE BILLIONAIRES
new_list = []
url = "https://www.geonames.org/search.html?q="  # website for retrieve the residence state from the residence city

country_world = pd.read_csv("countries and continents.csv") # this dataset is used only for classify the residence continents of billionaires
country_world = country_world[["name","Continent"]]

for el in category_list:
    
    try:
        # manual imputation of US states, which are not present in the country_world. Here you can only find US
        
        if 'state' in el:
            if len(USA_GDP[USA_GDP['GeoName'] == el['state']])>0:
                #print(f"-->{el['personName']}-->{el['state']} NA-->United States")
                
                el['continent'] = "NA"
                el['residence_state'] = "United States"
        else:        
            if 'city' not in el:
                continue
                
            r = requests.get(url+el['city']+"&country=")
            soup = BeautifulSoup(r.content)
            row = soup.find_all('td')

            if len(row)>=6:
                path = row[5].get_text(separator=' ')

                residence_city = path.split(',')[0]
                continent = country_world[country_world['name']==residence_city.strip()]
            
                if len(continent)>0 and isinstance(continent['Continent'].item(), str)==False and math.isnan(continent['Continent'].item()):
                        el['continent'] = ""
                        el['residence_state'] = state
                
                elif len(continent)>0:
                    # bug fixing for Canada, this states wasn't matched in the country_world dataset
                    
                    if residence_city.strip() == 'Canada':
                        #print(f"-->{el['personName']}--> {el['city']} --> NA -->{residence_city.strip()}")

                        el['continent'] = "NA"
                        el['residence_state'] = residence_city.strip()
                    else:
                        state = path.split(',')[0]
                        el['continent'] = continent['Continent'].item()
                        el['residence_state'] = residence_city.strip()

                        #print(f"-->{el['personName']}--> {el['city']} -->{continent['Continent'].item()}-->{state}")
                 
                 
                else:
                    el['continent'] = ""
                    el['residence_state'] = ""
                    
    except KeyError:   
        continue    

# BUG FIXING RELATED TO NO MATCHED STATES <true.json<->world_gdp> AND BLANK SPACE CHARACTER
for i in category_list:
    
    if 'residence_state' in i and i['residence_state'].strip() == "Russia":
        i['residence_state'] = "Russian Federation"
    if 'residence_state' in i and i['residence_state'].strip() == "Slovakia":
        i['residence_state'] = "Slovak Republic"
    for j in world_GDP['Country Name']:
        if 'residence_state' in i:
            if i['residence_state'].strip() == j:
                i['residence_state'] = i['residence_state'].strip()
                continue