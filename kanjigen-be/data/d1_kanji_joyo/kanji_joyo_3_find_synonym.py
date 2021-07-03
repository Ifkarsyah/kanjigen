import csv

from pprint import pprint as print
from collections import Counter

with open("kanji_joyo_output.csv") as f:
    rows = csv.reader(f, delimiter=",")
    next(rows)
    meanings = [r[2] for r in rows]

    meanings = sorted(meanings)

    len_meanings = len(meanings)
    d = Counter(meanings)
    for key, cnts in list(d.items()):  # list is important here
        if cnts <= 2:
            del d[key]
    print(d)
