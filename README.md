
# Billionaires-GDPproCapita-analysis

**Objective** : The project aims to investigate whether the presence of billionaires in a country (or its regions/provinces) leads to an increase in the country's wealth measured by GDP per capita. Data from Forbes magazine's billionaire rankings are used for this analysis.

**Data** : The data includes information on each billionaire's asset growth from 2014 to 2021, residence, age, gender, and industry (from Forbes) and GDP per capito for eache state, american state and european region (From world bank, census, kaggle and ec.europa).

**Territorial Analysis**: The analysis considers the billionaire's wealth in relation to both the country's GDP and the GDP of specific regions or provinces. For Europe, the Nomenclature of Territorial Units for Statistics (NUTS) is used, dividing territories into three levels based on population.

**Focus**: The analysis focuses on Europe and the United States to compare the two regions known for their cultural and economic differences and the high number of billionaires.

**Time Period**: The analysis covers data up to 2021, as GDP data for 2022 was not available at the time of data collection. The analysis starts from 2014, as most billionaires listed in the rankings joined recently.

**Research Questions**:

1) Do countries with more billionaires have higher average GDP per capita?
2) Which billionaires have the highest correlation between their wealth trend and the GDP per capita trend of their region/state?
3) What is the percentage of women billionaires in the top 10 richest countries (with the highest average GDP per capita)?

_____________________________

## How it is structured:
 
- All the dataset are into exported and final folders.
- Each file contains all the transformations done on that specific dataset.
- We create a [main file][] which you can run for compute all the files toghether.
- The modified datasets have been merged toghether into MongoDB (a no relational database which store files into json format). (check the pipeline [here][])
- The final dataset obtained has been used for answer to the three research questions.(check [here][] for the results)

