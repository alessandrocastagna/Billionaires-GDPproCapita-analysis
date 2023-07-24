import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)
from unidecode import unidecode
from data_acquisition import *
from data_cleaned_enriched_import import *

## Creation of the middle table between european_bill_byProvince.json and true.json
# COSINE SIMILARITY FUNCTION
def similarity(X,Y):
    
    X_list = word_tokenize(X)  
    Y_list = word_tokenize(Y)
    l1 =[]
    l2 =[]
    union=X_list+Y_list
    
    for w in union:
        if w in X_list:
            l1.append(1)
        else:
            l1.append(0)
        if w in Y_list: 
            l2.append(1)
        else: 
            l2.append(0)
    # cos formula 
    c = 0
    for i in range(len(union)):
            c+= l1[i]*l2[i]
    #cosine = c / float((sum(l1)*sum(l2))**0.5)
    d1=0
    for i in l1:
        d1+=i**2
    d1=d1**0.5
    d2=0
    for i in l2:
        d2+=i**2
    d2=d2**0.5
    if float(d1*d2) != 0:
        cos = c / float(d1*d2)
    else:
        cos = 0
    return(cos)


# DICTIONARY CREATION ['billionaire', 'provincia europa formato dataset_GDP_europeo']
eur_prov_matched = {}
for el in european_bill_byProvince:  
    max_val = -1
    index = 0
    for i in region_GDP['TIME']:
        # google translator function used for translate into English the european provincies of region_GDP (which are not the same of eur dictionary)
        par = GoogleTranslator(source='auto', target='en').translate(text=i).replace("-", " ") # translation and blank space removement
        par = par.replace("/", " ") # '/' removement
        
        string =  european_bill_byProvince[el].lower().replace("-", " ")
        string =  string.replace("/", " ")
        
        x = similarity(string.lower(),par.lower())
        
        
        if x > max_val:
            index = i
            max_val = x
    print (f"{el}:[{string.lower()},{index}]->{max_val}")
    
    if max_val > 0:
        eur_prov_matched[el] = index
    else:
        eur_prov_matched[el] = ''
    

## Manual imputation of missing values on which similarity doesn't work
for i in european_bill_byProvince:
    city = european_bill_byProvince[i].strip()

    if city == "Vienna Vienna":
        for j in eur_matched:
            if i == j:
                eur_matched[j] = 'Wien'

    elif city == "Valencia Valencia":
        for j in eur_matched:
            if i == j:
                eur_matched[j] = 'Comunitat Valenciana'

    elif city == "București Municipiul Bucureşti":
        for j in eur_matched:
            if i == j:
                eur_matched[j] = 'Bucuresti - Ilfov'

    elif city == "Mazovia Warszawa":
        for j in match:
            if i == j:
                eur_matched[j] = 'Warszawski stoleczny'

    elif city == "Bratislavský Kraj":
        for j in eur_matched:
            if i == j:
                eur_matched[j] = 'Bratislavský kraj'

    elif city == "Hesse Regierungsbezirk Gießen":
        for j in eur_matched:
            if i == j:
                eur_matched[j] = 'Gießen'

for i in eur_prov_matched:
    i['nome']=unidecode(i['nome'])

