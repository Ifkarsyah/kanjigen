import csv

from pprint import pprint as print
from collections import Counter
import csv
import requests

url = "https://kanjiapi.dev/v1/kanji/"


with open("s7_edges_kanji_radical.csv") as fin:
    rows = csv.reader(fin, delimiter=",")
    next(rows)

    results = []
    i = 0

    for j in range(3528):
        next(rows)
        i += 1

    # for row in rows:
    #     kanji, radicals = row
    #     print(row)
    #     assert 1 == 0

    with open("s5_kanjis_output.csv", mode="a") as fout:
        for row in rows:
            kanji, radicals = row
            resp = requests.get(url + kanji).json()
            element = {
                "kanji": kanji,
                "meanings": ":".join(resp["meanings"]),
            }

            results += [element]

            fout.write(element["kanji"])
            fout.write(",")
            fout.write(element["meanings"])
            fout.write("\n")

            i += 1
            print(i)
