### A program to scrape a single table from one page and import it into a csv file

from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/Strictly_Come_Dancing_(series_1)'
series_table = 'wikitable'

response = requests.get(wiki_url).text
Soup = BeautifulSoup(response, 'html.parser')

series_1_table = Soup.find_all('table')
table = Soup.find('table', class_='wikitable sortable')

#### Defining of the dataframe
df = pd.DataFrame(columns=['Couple', 'Score', 'Dance'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        couple = columns[0].text.strip()
        score = columns[1].text.strip()
        dance = columns[2].text.strip()
        
        df = df.append({'Couple': couple, 'Score': score, 'Dance': dance}, ignore_index=True)

df2 = pd.DataFrame(df)

print(df)