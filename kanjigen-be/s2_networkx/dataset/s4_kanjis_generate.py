import csv

from pprint import pprint as print
from collections import Counter
import csv
import requests

url = "https://kanjiapi.dev/v1/kanji/"


with open("s7_edges_kanji_radical.csv") as f:
    rows = csv.reader(f, delimiter=",")
    next(rows)

    results = []
    for row in rows:
        kanji, radicals = row
        resp = requests.get(url + kanji).json()
        element = {
            "kanji": kanji,
            "meanings": ":".join(resp["meanings"]),
        }

        results += [element]
        print(len(results))

with open("s5_kanjis_output.csv", mode="w") as f:
    fieldnames = ["kanji", "meanings"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
