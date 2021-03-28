import requests
import csv
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji'
resp = requests.get(url).text

soup = BeautifulSoup(resp, 'lxml')
table = soup.find('table', {'class': 'wikitable'})

header = [th.text.rstrip() for th in table.find_all('th')]

data = []

for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) != 9:
        continue
    num, kanji, _, _, _, _, _, meaning, _ = cells

    num = num.find(text=True)
    kanji = kanji.find('a').text
    meaning = meaning.find(text=True)

    data.append( {'num': num, 'kanji': kanji, 'meaning': meaning} )

with open('kanji_output.csv', mode='w') as file:
    fieldnames = ['num', 'kanji', 'meaning']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
