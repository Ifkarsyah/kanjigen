import csv

from pprint import pprint as print
from collections import Counter
import csv
import requests

url = "https://kanjiapi.dev/v1/kanji/"


with open("kanji_joyo_2_output_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    next(rows)

    results = []

    for row in rows:
        num, kanji, meaning = row

        resp = requests.get(url + kanji).json()

        grade = resp["grade"]
        jlpt = resp["jlpt"]
        unicode = resp["unicode"]
        meanings = resp["meanings"]
        readings = resp["kun_readings"] + resp["on_readings"]

        meanings = ":".join(meanings)
        readings = ":".join(readings)

        element = {
            "num": num,
            "kanji": kanji,
            "meanings": meanings,
            "grade": grade,
            "jlpt": jlpt,
            "unicode": unicode,
            "readings": readings,
        }

        results += [element]
        print(len(results))

with open("kanji_joyo_4_output_enriched.csv", mode="w") as f:
    fieldnames = ["num", "kanji", "meanings", "grade", "jlpt", "readings", "unicode"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
