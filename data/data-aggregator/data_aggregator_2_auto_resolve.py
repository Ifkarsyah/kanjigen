import csv
import requests

from bs4 import BeautifulSoup
from pprint import pprint


def get_true_radicals_list():
    true_radicals_list = set()

    with open('japanese-322-radicals.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            _, _, kanji, _, _, _, _, _, _, _ = row
            true_radicals_list.add(kanji)

    return true_radicals_list


true_radicals_list = get_true_radicals_list()

data = []

with open('kanji_total_1_raw.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, num, meaning, radicals, kanji_in_concept_meaning, h2_concept, h3_concept = row
        # solve 1: no radical problem
        if radicals == "":
            if kanji in true_radicals_list:
                radicals = kanji
            else:
                radicals = kanji
                # todo: temp-something with encoding issue, must be radicals = 'MANUAL'

        # solve 2: there exist strange char .
        radicals = radicals.replace('.', '')

        # solve 3: concept handling
        if kanji_in_concept_meaning != "":
            meaning = kanji_in_concept_meaning

        # solve 4: default meaning
        if meaning == "DEFAULT":
            if kanji == "快":
                meaning = "pleasure"
            elif kanji == "牛":
                meaning = "cow"

        row_after = {
            'num': num,
            'kanji': kanji,
            'radicals': radicals,
            'meaning': meaning,
            'concept': h2_concept,
            'subconcept': h3_concept,
        }
        data.append(row_after)

with open('kanji_total_2_auto_resolve.csv', mode='w') as file:
    fieldnames = ['num', 'kanji', 'radicals',
                  'meaning', 'concept', 'subconcept']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
