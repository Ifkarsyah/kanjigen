import requests
import csv
from bs4 import BeautifulSoup
import json

from pprint import pprint

url = "https://en.wikipedia.org/wiki/List_of_kanji_by_concept"
resp = requests.get(url).text

soup = BeautifulSoup(resp, "html.parser")

tags = soup.find_all(["h2", "h3", "h4", "p"])
tags = [t for t in tags if len(t.attrs) == 0]


def get_concept(t):
    headline = t.find("span", {"class": "mw-headline"})
    concept = ""
    if headline:
        concept = headline.get("id")
    return concept


def get_one_paragraph(t):
    res = []
    span_list = t.find_all("span")
    for span in span_list:
        span_text = span.text.split(" ")
        if "/" in span_text:

            if span_text[1] == "/":
                count_synonym = sum([1 for x in span_text if not x.isascii()])
                if count_synonym == 1:
                    kanji_list = [span_text[0]]
                    meaning = "DEFAULT"
                else:
                    lim = 2 * (count_synonym - 1) + 1
                    kanji_list = span_text[0:lim:2]
                    meaning = " ".join(span_text[lim:]).rstrip(";")

                res += [{"kanji": k, "meaning": meaning} for k in kanji_list]

            else:
                # one kanji, different meaning, '/' found in meaning
                kanji_list = [span_text[0]]
                meaning = " ".join(span_text[1:])

                res += [{"kanji": span_text[0], "meaning": meaning}]
        else:
            kanji, *meaning_list = span_text
            meaning = " ".join(meaning_list).rstrip(";")
            kanji_list = [kanji]
            res += [{"kanji": kanji, "meaning": meaning}]
    return res


h2_curr = ""
h3_curr = ""
h4_curr = ""
level_curr = 2  # 2,3,4

data_h2_h3_h4 = {}

for t in tags:

    if t.name == "h2":
        h2_curr = get_concept(t)
        data_h2_h3_h4[h2_curr] = {}
        curr_level = 2

    elif t.name == "h3":
        h3_curr = get_concept(t)
        data_h2_h3_h4[h2_curr][h3_curr] = {}
        curr_level = 3

    elif t.name == "h4":
        h4_curr = get_concept(t)
        data_h2_h3_h4[h2_curr][h3_curr][h4_curr] = {}
        curr_level = 4

    elif t.name == "p":  # 1 p == 1 category
        kanji_list = get_one_paragraph(t)

        if len(kanji_list) > 0:
            if curr_level == 2:
                data_h2_h3_h4[h2_curr]["kanji_list"] = kanji_list
            elif curr_level == 3:
                data_h2_h3_h4[h2_curr][h3_curr]["kanji_list"] = kanji_list
            elif curr_level == 4:
                data_h2_h3_h4[h2_curr][h3_curr][h4_curr]["kanji_list"] = kanji_list


with open("theme_3_output_raw.json", "w", encoding="utf8") as json_file:
    json.dump(data_h2_h3_h4, json_file, ensure_ascii=False)
