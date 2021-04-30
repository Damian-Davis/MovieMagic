import csv
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('div', attrs={'class': 'mw-content-ltr'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text.replace('\n', ' '))
    list_of_rows.append(list_of_cells)

outfile = open("film.csv", "w")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
