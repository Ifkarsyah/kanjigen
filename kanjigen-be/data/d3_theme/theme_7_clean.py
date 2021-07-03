import csv

from pprint import pprint as print
from collections import Counter
import csv
import requests

url = "https://kanjiapi.dev/v1/kanji/"


with open("theme_6_output_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    next(rows)

    results = []

    for row in rows:
        kanji, meaning, concept, subconcept = row

        meaning_clean = None
        if "," in meaning:
            try_remove = meaning.replace(",", "")
            if try_remove.isdigit():
                meaning_clean = try_remove
            else:
                meaning_clean = meaning.replace(" ", "")
                meaning_clean = meaning_clean.replace(",", "")

        if meaning_clean:
            meaning = meaning_clean

        element = {
            "kanji": kanji,
            "meaning": meaning,
            "theme": concept,  # also rename concept -> theme
            "subtheme": subconcept,
        }
        results += [element]

with open("theme_8_output_clean.csv", mode="w") as f:
    # also rename concept -> themes
    fieldnames = ["kanji", "meaning", "theme", "subtheme"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
