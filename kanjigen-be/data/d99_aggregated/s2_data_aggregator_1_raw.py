from pprint import pprint
import csv

data = dict()

with open("s1_input_d1_kanji_joyo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        num, kanji, meanings, grade, jlpt, readings, unicode = row
        data[kanji] = {"num": num, "meanings": meanings, "grade": grade, "jlpt": jlpt}

assert len(data) == 2136

with open("s1_input_d2_radicals.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, radical_list = row
        if kanji in data:
            data[kanji]["radicals"] = radical_list

with open("s1_input_d3_theme.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, meaning, theme, subtheme = row
        if kanji in data:
            data[kanji]["kanji_in_theme_meaning"] = meaning
            data[kanji]["theme"] = theme
            data[kanji]["subtheme"] = subtheme


data = sorted(data.items(), key=lambda x: int(x[1]["num"]))

data = [
    {
        "num": v["num"],
        "kanji": k,
        "meanings": v.get("meanings"),
        "radicals": v.get("radicals"),
        "kanji_in_theme_meaning": v.get("kanji_in_theme_meaning"),
        "theme": v.get("theme"),
        "subtheme": v.get("subtheme"),
    }
    for k, v in data
]


with open("s3_kanji_total_1_raw.csv", mode="w") as file:
    attribs = [
        "num",
        "meanings",
        "radicals",
        "kanji_in_theme_meaning",
        "theme",
        "subtheme",
    ]
    fieldnames = ["kanji"] + attribs
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
